#!/bin/bash
set -e

docker rm -f clair-adapter || true
docker rm -f clair || true
docker run -d --name clair -p 6060:6060 -v $(pwd)/config/clair/config.yml:/etc/clair/config.yaml \
goharbor/clair-photon:dev
docker run -d --name clair-adapter -p 8084:8080 --env-file $(pwd)/config/clair/adapter_env \
goharbor/clair-adapter-photon:dev
