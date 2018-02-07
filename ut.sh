#!/bin/bash

pkg=github.com/vmware/harbor/src/$1
mysql_host=127.0.0.1
mysql_port=3307
mysql_username=root
mysql_password=root123
mysql_database=registry

MYSQL_HOST=$mysql_host MYSQL_USR=$mysql_username \
MYSQL_PORT=$mysql_port MYSQL_PWD=$mysql_password \
MYSQL_DATABASE=$mysql_database go test -v $pkg
