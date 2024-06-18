# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install Poetry
RUN pip install poetry

# Install other dependencies
RUN apt-get update && apt-get install -y gcc
#RUN pip install uvicorn haversine

# Install project dependencies
RUN poetry config virtualenvs.create false
RUN poetry install

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["poetry", "shell", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
