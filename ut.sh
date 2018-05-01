#!/bin/bash

pkg=github.com/vmware/harbor/src/$1
db_host=127.0.0.1
db_port=5432
db_username=postgres
db_password=root123
db_database=registry

POSTGRESQL_HOST=$db_host \ 
POSTGRESQL_PORT=$db_port \
POSTGRESQL_USR=$db_username \ 
POSTGRESQL_PWD=$db_password \
POSTGRESQL_DATABASE=$db_database go test -v $pkg
