#!/bin/bash

# Render startup script
echo "Starting Gemini Balance application..."

# Set environment variables
export PORT=${PORT:-8000}

# Ensure data directories exist
mkdir -p data
mkdir -p logs

# Start application
echo "Starting application on port $PORT..."
exec uvicorn app.main:app --host 0.0.0.0 --port $PORT --no-access-log
