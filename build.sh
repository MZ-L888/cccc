#!/bin/bash

# Render build script
echo "Starting Gemini Balance build..."

# Check Python version
echo "Using Python version: $(python --version)"

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Run initialization script
echo "Running environment initialization..."
python init_render.py

# Set permissions
echo "Setting file permissions..."
chmod +x app/main.py
chmod +x start.sh

echo "Build completed successfully!"
