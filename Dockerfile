# Base image
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    pkg-config \
    default-libmysqlclient-dev

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "--workers=4", "--threads=4", "--bind=0.0.0.0:8000", "config.wsgi:application"]
# CMD ["gunicorn", "--workers=4", "--threads=4", "--bind=0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "config.asgi:application"]
