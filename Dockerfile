# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY backup.py /app/backup.py

# Set default environment variables (you can override these when running the container)
ENV SOURCE_FOLDER=/data/source
ENV BACKUP_FOLDER=/data/backup

# Create data directories
# RUN mkdir -p ${SOURCE_FOLDER} ${BACKUP_FOLDER}

# Run the script by default
CMD ["python", "/app/backup.py"]
