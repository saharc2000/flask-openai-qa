import os
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_URL = os.getenv("DATABASE_URL")
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')