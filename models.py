from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = Base.metadata

class qaEntry(Base):
    __tablename__ = 'qa_entry'

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)

    def __repr__(self):
        return f'id = {self.id}, question = {self.question}, answer = {self.answer}'

