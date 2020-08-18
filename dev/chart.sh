#!/bin/bash
set -e

docker rm -f chart || true
docker run -d --name chart -p 9999:9999 -v $(pwd)/data/chart:/chart_storage \
--env-file $(pwd)/config/chart/env goharbor/chartmuseum-photon:dev
