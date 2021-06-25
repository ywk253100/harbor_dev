#!/bin/bash

pkg=github.com/goharbor/harbor/src/$1
func=$2

arg=$pkg
if [[ -n $func ]]
then
    arg="$pkg -run $func"
fi

POSTGRESQL_HOST=127.0.0.1 \
POSTGRESQL_PORT=5432 \
POSTGRESQL_USR=postgres \
POSTGRESQL_PWD=root123 \
POSTGRESQL_DATABASE=registry \
POSTGRES_MIGRATION_SCRIPTS_PATH=/Users/yinw/workspace/src/github.com/goharbor/harbor/make/migrations/postgresql \
go test -v -race $arg
