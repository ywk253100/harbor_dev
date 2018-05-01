#!/bin/bash
set -e

source common.sh

image=vmware/harbor-db:dev
name=harbor_dev_postgres
port=5432
password=root123
postgres_data=$data/database

docker rm -f $name || true
docker run -d --name $name -p $port:5432 -v $postgres_data:/var/lib/postgresql/data \
-e POSTGRES_PASSWORD=$password $image
