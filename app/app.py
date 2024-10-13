from flask import Flask, request, jsonify
from models import qaEntry
from logger import logger  #maybe change
from database import DataBase
from services import OpenAIService
from config import Config

def create_app(test_config=None):
    app = Flask(__name__)
    if test_config:
        app.config.update(test_config)
    else:
        app.config.from_pyfile('config.py')  # Default config

    database = DataBase()
    service = OpenAIService()

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

#add git ignore