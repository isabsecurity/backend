# Base image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Run both Django and bot using a custom script
CMD ["bash", "-c", "python manage.py runserver 0.0.0.0:8000 & python manage.py bot"]
