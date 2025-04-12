#!/bin/bash
# deploy.sh - Deploy the project using Docker Compose

echo "Deploying the Scalable UDP Server project using Docker Compose..."
docker-compose up --build -d
echo "Deployment complete. Use 'docker-compose logs -f' to view the logs."
