#!/bin/bash
set -e

docker rm -f postgres || true
docker run -d --name postgres -p 5432:5432 -v $(pwd)/data/postgres:/var/lib/postgresql/data \
goharbor/harbor-db:dev
