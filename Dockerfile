FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Make entrypoint script executable
RUN chmod +x entrypoint.sh
# Command to makemigrations, migrate the database, and start the notetaker app
CMD ["sh", "-c", "./entrypoint.sh"]