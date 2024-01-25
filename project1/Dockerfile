# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY app.py /app/

# Install Flask and expose the port
RUN pip install flask && \
    apt-get update && apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Expose the port that Flask will run on
EXPOSE 8000

# Define the command to run your application
CMD ["python", "app.py"]
