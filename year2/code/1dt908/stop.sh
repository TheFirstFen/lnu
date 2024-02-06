#!/bin/bash

OS=$(uname -s)

case "$OS" in
    Linux*)     DOCKERFILE_PATH="Docker_Linux/";;
    Darwin*)    DOCKERFILE_PATH="Docker_Mac/";;
    CYGWIN*|MINGW32*|MSYS*|MINGW*) DOCKERFILE_PATH="Docker_Windows/";;
    *)          echo "Unsupported operating system: $OS"; exit 1;;
esac

cd $DOCKERFILE_PATH

docker-compose down

if [ $? -eq 0 ]; then
    echo "Docker-compose stop successful."
else
    echo "Docker-compose stop failed."
fi
