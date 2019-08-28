#!/bin/bash
set -e

source common.sh

image=registry:2.6.0
name=harbor_dev_registry
registry_data=$data/registry/
config=$codes/make/common/config/registry
ui_ip=$local_host_ip
if [ -n $1 ]
then
    ui_ip=$1
fi

sed -i -r s%"realm:.*"%"realm: http://${ui_ip}:8080/service/token"% $config/config.yml
sed -i -r s%"url:.*"%"url: http://${ui_ip}:8080/service/notifications"% $config/config.yml

docker rm -f $name || true
docker run -d --name $name -p $registry_port:5000 -v $registry_data:/storage \
-v $config:/etc/registry/ $image serve /etc/registry/config.yml
