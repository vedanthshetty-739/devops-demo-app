FROM python:3.12-slim

# Install system dependencies (for pip builds etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*


# Copy dependency files first for better caching
COPY requirements.txt ./requirements.txt
     

# Install uv package manager
RUN pip install -r requirements.txt

# Set working directory
WORKDIR /app

# Copy application code
COPY src/ .
# COPY tests/ ./tests #if this needed then remove it from .dockerignore

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI (main.py inside src)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
