# Use the 'slim' base image for better support for pre-compiled packages
FROM --platform=linux/amd64 python:3.10-slim-bullseye

# Install the single system library needed by lightgbm for parallel processing
RUN apt-get update && apt-get install -y --no-install-recommends libgomp1

# Set the working directory inside the container
WORKDIR /app

# Copy and install the Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the necessary application scripts and the pre-trained models
# This includes your 1A processor, your 1B processor, and all trained models
COPY process_pdfs.py .
COPY process_1b.py .
COPY models/ ./models/

# Set the command to run when the container starts
# This will execute your final Round 1B script
CMD ["python", "process_1b.py"]