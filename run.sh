#!/bin/bash

echo "Installing requirements..."
pip install -r requirements.txt

echo ""
echo "Starting DrawStore Loader..."
python app.py
