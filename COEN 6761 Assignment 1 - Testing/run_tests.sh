#!/bin/bash

echo "Running unit tests..."
python3 -m unittest discover -s tests -p "test_*.py"

echo "Generating code coverage report..."
pip install coverage
coverage run -m unittest discover -s tests -p "test_*.py"
coverage report -m
