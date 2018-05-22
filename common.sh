#!/bin/bash
set -e

remote_host_ip=10.117.169.13
local_host_ip=$(ifconfig en10 | awk '/inet /{print substr($2,0)}')

codes=/Users/yinw/workspace/src/github.com/vmware/harbor
data=/data
encrypt_key=$data/secretkey

# secret
ui_secret=ui_secret
jobservice_secret=jobservice_secret

adminserver_port=8888
adminserver=http://127.0.0.1:$adminserver_port
registry_port=5000
registry=$remote_host_ip:$registry_port
database_host=$remote_host_ip
database_port=3307
#database_port=5432
#database_username=postgres
database_username=root
database_password=root123
database_registry=registry
database_clair=postgres

log_level=debug
