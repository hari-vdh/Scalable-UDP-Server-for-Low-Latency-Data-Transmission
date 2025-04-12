#!/bin/bash
# setup.sh - Sets up the project environment

echo "Setting up the environment for the Scalable UDP Server project..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setup complete. To activate the environment, run: source venv/bin/activate"
