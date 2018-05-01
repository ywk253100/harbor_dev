#!/bin/bash
set -e

source common.sh
cd $harbor

build_args="--no-cache --build-arg HTTP_PROXY=http://proxy.vmware.com:3128 --build-arg HTTPS_PROXY=http://proxy.vmware.com:3128"

postgresql_path=$harbor/make/photon/postgresql
docker build $build_args -f $postgresql_path/Dockerfile -t vmware/postgresql-photon:dev $postgresql_path/

db_path=$harbor/make/photon/db/postgresql
sed -i 's/__postgresql_version__/dev/g' $db_path/Dockerfile
docker build $build_args -f $db_path/Dockerfile -t vmware/harbor-db:dev $db_path/
sed -i 's/dev/__postgresql_version__/g' $db_path/Dockerfile
