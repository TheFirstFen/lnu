#!/bin/bash

# Get the operating system
OS=$(uname -s)

# Define the Dockerfile path based on the operating system
case "$OS" in
    Linux*)     DOCKERFILE_PATH="Docker_Linux/";;
    Darwin*)    DOCKERFILE_PATH="Docker_Mac/";;
    CYGWIN*|MINGW32*|MSYS*|MINGW*) DOCKERFILE_PATH="Docker_Windows/";;
    *)          echo "Unsupported operating system: $OS"; exit 1;;
esac

# Move to the Dockerfile directory
cd $DOCKERFILE_PATH

# Build the Docker image using the selected Dockerfile
# docker build -t my_mysql_image_proj_1dt908 .
docker-compose up -d

# Check if Docker build was successful
if [ $? -eq 0 ]; then
    echo "Docker build successful."
else
    echo "Docker build failed."
fi

# Run the Docker image
# docker run -d --name my_mysql_container_proj_1dt908 -p 3307:3307 my_mysql_image_proj_1dt908

# Check if Docker run was successful
if [ $? -eq 0 ]; then
    echo "Docker run successful."
else
    echo "Docker run failed."
fi
