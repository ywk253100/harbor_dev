#!/bin/bash
set -e

harbor=/root/workspace/src/github.com/vmware/harbor
ip=$(ifconfig ens33 | awk '/inet /{print substr($2,0)}')
data=/data
key=$data/secretkey
ui_secret=ui_secret
jobservice_secret=jobservice_secret
