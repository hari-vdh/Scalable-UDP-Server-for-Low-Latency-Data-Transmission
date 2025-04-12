#!/bin/bash
# run_tests.sh - Execute unit tests

echo "Running tests for the Scalable UDP Server project..."
source venv/bin/activate
python -m unittest discover tests
