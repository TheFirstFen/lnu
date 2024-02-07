#!/bin/bash

OS=$(uname -s)

case "$OS" in
    Linux*)     DOCKERFILE_PATH="Docker_Linux/";;
    Darwin*)    DOCKERFILE_PATH="Docker_Mac/";;
    CYGWIN*|MINGW32*|MSYS*|MINGW*) DOCKERFILE_PATH="Docker_Windows/";;
    *)          echo "Unsupported operating system: $OS"; exit 1;;
esac

cd $DOCKERFILE_PATH

docker-compose up -d

if [ $? -eq 0 ]; then
    echo "Docker-compose build & run successful."
    docker inspect docker_linux_db_1 | jq -r '.[].NetworkSettings.Networks.docker_linux_default.IPAddress'
else
    echo "Docker-compose build & run failed."
fi
