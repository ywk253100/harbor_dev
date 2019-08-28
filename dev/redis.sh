#!/bin/bash
set -e

docker rm -f redis || true
docker run -d --name redis -p 6379:6379 -v $(pwd)/data/redis:/var/lib/redis \
goharbor/redis-photon:dev
