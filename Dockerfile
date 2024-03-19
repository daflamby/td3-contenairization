# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY app.py .

# Install dependencies (requests library)
RUN pip install requests

# Run the Python script when the container starts
CMD ["python", "app.py"]
