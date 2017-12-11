#!/bin/bash
set -e

source common.sh

adminserver=127.0.0.1:8888
binary=$harbor/src/ui/ui
private_key=$harbor/make/common/config/ui/private_key.pem
ui_config=$harbor/make/common/config/ui/app.conf
cp $private_key /etc/ui/private_key.pem

LOG_LEVEL=debug \
UI_SECRET=$ui_secret \
JOBSERVICE_SECRET=$jobservice_secret \
CONFIG_PATH=$ui_config \
ADMINSERVER_URL=$adminserver KEY_PATH=$key $binary
