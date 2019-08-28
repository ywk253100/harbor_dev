#!/bin/bash
set -e

docker rm -f portal || true
docker run -d --name portal -p 8082:8080 goharbor/harbor-portal:dev
