from flask import Flask, request, jsonify
from models import qaEntry
from logger import logger  #maybe change
from database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#change to app.py
import os
from openai import OpenAI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#class config.py


DATABASE_URL = "postgresql://postgres:123@insait-io-project-db-1:5432/alembic_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
Base.metadata.create_all(engine)

# Initialize the database
# db.init_app(app)
# with app.app_context():
#     db.create_all()  # Create tables in the database

client = OpenAI(
    # This is the default and can be omitted
    api_key = os.getenv('OPENAI_API_KEY')
)


@app.route('/ask', methods=['POST'])
def ask_question():
    session = SessionLocal()
    try:
        data = request.get_json()
        question = data.get('question')
    except Exception as e:
        logger.error(f"Error while parsing the request: {e}")
        return jsonify({"error": "Invalid input."}), 400
    # לעטוף בtry except
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="gpt-3.5-turbo",
        max_tokens=50,
    )
    print(response.choices[0].message.content)

    answer = response.choices[0].message.content
    # Store question and answer in the database
    logger.info(f'question: {question}, answer: {answer}')
    qa = qaEntry(question=question, answer=answer)
    try:
        session.add(qa)
        session.commit()
        logger.info(f'qa committed')
    except Exception as e:
        logger.error(f"Error while adding question-answer: {e}")
        return jsonify({"error": "Unable to save the question and answer."}), 500
    # entry = session.query(QaEntry).first()
    # print(entry)
    return jsonify({"question": question, "answer": answer}), 201

#add git ignore