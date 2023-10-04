# Use an official Python runtime as the parent image
FROM  python:3.12-alpine3.18

# Install plugins
RUN apk add bash

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and any other dependencies (assuming you have a requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask to run in production mode
ENV FLASK_APP=main
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Run app.py when the container launches
ENTRYPOINT ["flask", "--app", "main", "--debug", "run"]
