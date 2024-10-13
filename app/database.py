from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config

class DataBase():
    def __init__(self):
        self.DATABASE_URL = Config.DATABASE_URL
        self.engine = create_engine(self.DATABASE_URL)
        self.SessionLocal = sessionmaker(bind=self.engine)

        Base = declarative_base()
        Base.metadata.create_all(self.engine)

    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
