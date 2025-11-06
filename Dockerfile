# Use a maintained Python image
FROM python:3.9-slim-bookworm

# Install system dependencies
RUN apt-get update && \
    apt-get install -y git curl ffmpeg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --no-cache-dir -U pip

# Copy app files
COPY . /app/
WORKDIR /app/

# Install requirements
RUN pip install --no-cache-dir -U -r requirements.txt

# Run your app
CMD ["bash", "start.sh"]
