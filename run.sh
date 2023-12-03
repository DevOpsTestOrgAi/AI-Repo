#!/bin/bash

# Install required packages
pip install -r requirements.txt

# Build and run the Docker container
docker-compose up --build
