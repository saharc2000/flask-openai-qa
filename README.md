## Project Overview

This repository contains a Flask-based backend application designed as a home assignment for Insait's Backend Internship. The application provides an API endpoint to ask questions, leveraging the OpenAI API to fetch answers and storing both the questions and answers in a PostgreSQL database. The entire application is containerized using Docker and orchestrated with Docker Compose, facilitating easy deployment and management of services.

## Features

- **Flask Server**: Lightweight Flask server exposing an /ask endpoint for handling incoming questions.
- **OpenAI API Integration**: Utilizes the OpenAI API for intelligent responses, powered by the OpenAI Python client library.
- **PostgreSQL Database**: Employs PostgreSQL for reliable storage of questions and answers.
- **Database Migrations**: Uses Alembic for smooth schema updates without data loss.
- **Dockerized Environment**: Full dockerization of both Flask application and PostgreSQL database.
- **Docker Compose**: Simplifies management of multiple services in isolated containers.
- **Automated Testing**: Includes pytest for ensuring API endpoint functionality and code reliability.

## Technology Stack

- Backend: Flask
- Database: PostgreSQL
- ORM: SQLAlchemy
- Migrations: Alembic
- Containerization: Docker
- Orchestration: Docker Compose
- Testing: pytest
- AI Integration: OpenAI API

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- PostgreSQL

This project uses Python and the required dependencies are managed through the requirements.txt file, which will be automatically installed during the Docker container build process.  
The Docker setup will handle the installation of these dependencies automatically when you build the containers.

### Setup

1. Clone the repository
```bash
git clone https://github.com/saharc2000/flask-openai-qa.git
cd flask-openai-qa
```

2. Set up environment variables
Create a .env file in the project root and add:
```
OPENAI_API_KEY=your_openai_api_key
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
DATABASE_URL=postgresql://your_db_user:your_db_password@db:5432/your_db_name
```
3. Build and run with Docker Compose
```
docker-compose up --build
```
4. Access the API
The API will be available at `http://localhost:5000/ask`

5. Database Migration with Alembic:  
 Alembic is a lightweight database migration tool for use with SQLAlchemy. It allows you to manage database schema changes over time in a systematic way.  
 To initialize your PostgreSQL database you should do the following:  
   a. Update Your Models  
    Before creating a migration, update your models.py file to reflect the changes you want in your database schema  
   b. Create a Migration  
    To create a new migration script, run the following command:  
    ```
    docker exec -it your_web_docker_name alembic revision --autogenerate -m "your_message"
    ```
   Notice: To find your_web_docker_name run:  
    ```
    docker ps
    ```
   This command generates a new migration file in the alembic/versions directory. Be sure to review the generated migration script to ensure it accurately reflects the 
   changes you intended.

   c. Apply the Migration
    To apply your migrations and update the database schema, run:
   ``` 
   docker exec -it  your_web_docker_name alembic upgrade head
   ```
   d. Check Migration Status
    To view the current migration status, you can run:
   ```
   docker exec -it  your_web_docker_name alembic current
   ```
   e. Downgrade a Migration (if needed)
    If you need to revert the last migration, you can use the following command:
   ```
   docker exec -it  your_web_docker_name alembic downgrade -1
   ```

7. Running Tests:
   Set up test environment variables
   Create a .env.test file in the project root and add:
   ```
   OPENAI_API_KEY=your_openai_api_key
   POSTGRES_DB=your_test_db_name
   POSTGRES_USER=your_db_user
   POSTGRES_PASSWORD=your_db_password
   DATABASE_URL=your_test_postgres_sql_url
   ```
  Execute the following command to run the test suite:
   ```
   docker-compose run web pytest
   ```
## API Documentation

### Ask Endpoint

- **URL**: /ask
- **Method**: POST
- **Body**:
```
{
 "question": "Your question here"
}
```
Success Response:
```
Code: 200
Content:
{
  "question": "Your question here",
  "answer": "AI-generated answer"
}
```
Please note: The question submitted cannot be empty and must contain no more than 50 words.
