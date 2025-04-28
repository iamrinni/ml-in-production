# Use official Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy the script into the container
COPY app.py .

# Run the script
CMD ["python", "app.py"]