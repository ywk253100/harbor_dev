#!/bin/bash
set -e

source common.sh

binary=$codes/src/core/core
token_private_key=$codes/make/common/config/ui/private_key.pem
ui_config=$codes/make/common/config/ui/app.conf

LOG_LEVEL=$log_level \
UI_SECRET=$ui_secret \
JOBSERVICE_SECRET=$jobservice_secret \
CONFIG_PATH=$ui_config \
ADMINSERVER_URL=$adminserver \
KEY_PATH=$encrypt_key \
TOKEN_PRIVATE_KEY_PATH=$token_private_key \
$binary
