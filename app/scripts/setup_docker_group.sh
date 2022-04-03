#!/bin/bash
set -e -x
{
    sudo groupadd -g 999 docker
    sudo usermod -aG docker $USER
    
    echo "Generated and activated docker group"
} || echo "Group already exists, skipping docker group generation."

export DOCKER_UID=$(id -u $USER)
export DOCKER_GID=$(cut -d: -f3 < <(getent group docker))
echo "done"
newgrp docker