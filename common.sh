#!/bin/bash
set -e

harbor=/root/workspace/src/github.com/vmware/harbor
ip=$(ifconfig eth0 | awk '/inet addr/{print substr($2,6)}')
data=/data
key=$data/secretkey
ui_secret=ui_secret
jobservice_secret=jobservice_secret