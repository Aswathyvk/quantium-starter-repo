#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate

# Run test suite
pytest test_app.py

# Capture exit code and propagate it
if [ $? -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Tests failed."
    exit 1
fi