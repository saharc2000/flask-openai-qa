FROM python:3.9-slim

# Set a working directory
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

# Use Gunicorn as the WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.app:create_app()"]