from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
metadata = Base.metadata

class qaEntry(Base):
    __tablename__ = 'qa_entry'

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    # date = Column(DateTime, default=func.now())

    # def __init__(self, question, answer):
    #     self.question = question
    #     self.answer = answer

    # def save(self):
    #     try:
    #         db.session.add(self)
    #         db.session.commit()
    #     except Exception as e:
    #         db.session.rollback()
    #         raise e


    def __repr__(self):
        return f'id = {self.id}, question = {self.question}, answer = {self.answer}'


#     from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class QAEntry(db.Model): 
#     __tablename__ = 'question_answer' 
#     id = db.Column(db.Integer, primary_key=True)
#     question = db.Column(db.String, nullable=False)
#     answer = db.Column(db.String, nullable=False)
    
#     def __init__(self, question, answer):
#         self.question = question
#         self.answer = answer

#     def save(self):
#         """Save the QAEntry to the database"""
#         try:
#             db.session.add(self)
#             db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             raise e
