from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Replace `postgres_container` with your actual PostgreSQL container name
DATABASE_URL = "postgresql://postgres:123@insaitioproject-db-1:5432/alembic_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Define a function to get a new session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
