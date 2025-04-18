# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy requirements file first to install dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the UDP port (matching config)
EXPOSE 4210

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run the UDP server
CMD ["python", "src/udp_server.py"]
