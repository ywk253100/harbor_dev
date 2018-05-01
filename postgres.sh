#!/bin/bash
set -e

source common.sh

image=vmware/postgresql-photon:v1.5.0-rc2
name=harbor_dev_postgres
port=5432
password=root123
postgres_data=$data/clair-db

docker rm -f $name || true
docker run -d --name $name -p $port:5432 -v $postgres_data:/var/lib/postgresql/data \
-e POSTGRES_PASSWORD=$password $image
