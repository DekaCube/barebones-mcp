# Use Python 3.13 slim bookworm as base image
FROM python:3.13-slim-bookworm

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY server.py .

# Expose the port the app runs on
EXPOSE 8000

# Run the server
CMD ["python", "server.py"]