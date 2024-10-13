import os
class Config:
    DATABASE_URL = os.getenv("DATABASE_URL")
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

class TestConfig:
    DATABASE_URL = os.getenv("DATABASE_URL")
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    TESTING = True