FROM python:3.11-slim

WORKDIR /app

# Copy requirements
COPY src/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY src/main.py .

# Expose port
EXPOSE 8080

# Run with gunicorn
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 main:app
#run 1
