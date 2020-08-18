#!/bin/bash
set -e

docker rm -f portal || true
docker run -d --name portal -v $(pwd)/config/portal/nginx.conf:/etc/nginx/nginx.conf -p 8082:8080 goharbor/harbor-portal:dev
