from flask import Flask, request, jsonify
from app.models import qaEntry
from app.logger import logger  #maybe change
from app.database import DataBase
from app.services import OpenAIService
from app.config import Config, TestConfig

def create_app(test_config=None):
    app = Flask(__name__)
    if test_config:
        print("Test config")
        config = TestConfig()
    else:
        config = Config()
        
    database = DataBase(config)
    service = OpenAIService(config)

    @app.route('/ask', methods=['POST'])
    def ask_question():
        try:
            data = request.get_json()
            question = data.get('question')
            if not question:
                raise ValueError("No question provided.")
        except Exception as e:
            logger.error(f"Error while parsing the request: {e}")
            return jsonify({"error": "Invalid input."}), 400
        try:
            answer = service.get_answer_from_openai(question)
            logger.info(f'question: {question}, answer: {answer}')
            qa = qaEntry(question=question, answer=answer)
            with next(database.get_db()) as session:
                session.add(qa)
                session.commit()
                logger.info(f'qa committed')
        except Exception as e:
            session.rollback()
            logger.error(f"Error while adding question-answer: {e}")
            return jsonify({"error": "Unable to save the question and answer."}), 500
        finally:
            session.close()

        entry = session.query(qaEntry).order_by(qaEntry.id.desc()).first()
        return jsonify({"question": entry.question, "answer": entry.answer}), 200
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000)

# The app.py file is the main entry point for the application. It creates a Flask app and defines the /ask route,
# which accepts a POST request with a JSON payload containing a question. The app then uses the OpenAIService
# to get an answer from the OpenAI API and saves the question-answer pair to the database using the DataBase class.
# Finally, it returns the question and answer in the response.