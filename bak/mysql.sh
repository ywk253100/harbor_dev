#!/bin/bash
set -e

source common.sh

image=vmware/harbor-db:dev
name=harbor_dev_mysql
port=3307
password=root123
mysql_data=$data/database

docker rm -f $name || true
docker run -d --name $name -p $port:3306 -v $mysql_data:/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD=$password $image