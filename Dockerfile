FROM python:3.9-slim

# Set a working directory
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

# Install dependencies
# RUN pip install -r requirements.txt 
# --no-cache-dir
# RUN alembic revision --autogenerate -m "Initial migration"
# RUN alembic upgrade head

# Use Gunicorn as the WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]
#gunicorn vs unvcorn