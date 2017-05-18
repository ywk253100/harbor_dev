#!/bin/bash
set -e

source common.sh

#image=vmware/registry:photon-2.6.0
image=registry:2.6.0
name=harbor_dev_registry
port=5000
registry_data=/data/registry/
config=$harbor/make/common/config/registry

sed -i -r s%"realm:.*"%"realm: http://$ip/service/token"% $config/config.yml
sed -i -r s%"url:.*"%"url: http://$ip/service/notifications"% $config/config.yml

docker rm -f $name || true
docker run -d --name $name -p $port:5000 -v $registry_data:/storage \
-v $config:/etc/registry/ $image serve /etc/registry/config.yml
