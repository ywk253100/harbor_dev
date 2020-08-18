#!/bin/bash
set -e

#external_url=http://10.117.180.27
#notification_service_url=http://127.0.0.2:8080
#if [ -n "$1" ]
#then
#    external_url=$1
#fi

#if [ -n "$2" ]
#then
#    notification_service_url=$2
#fi

#sed -i -r s%"realm:.*"%"realm: ${external_url}/service/token"% $(pwd)/config/registry/config.yml
#sed -i -r s%"url:.*"%"url: ${notification_service_url}/service/notifications"% $(pwd)/config/registry/config.yml

docker rm -f registry || true
docker run -d --name registry -p 5000:5000 -v $(pwd)/data/registry:/storage \
-v $(pwd)/config/registry/:/etc/registry/ goharbor/registry-photon:dev
