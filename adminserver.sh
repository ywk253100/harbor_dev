#!/bin/bash
set -e

source ./common.sh

port=8888
store=$data/config/config.json
binary=$harbor/src/adminserver/adminserver

LOG_LEVEL=debug \
EXT_ENDPOINT=http://$ip \
AUTH_MODE=db_auth \
SELF_REGISTRATION=on \
MYSQL_HOST=127.0.0.1 \
MYSQL_PORT=3307 \
MYSQL_USR=root \
MYSQL_PWD=root123 \
MYSQL_DATABASE=registry \
SQLITE_FILE= \
LDAP_URL=ldap://10.117.6.132 \
LDAP_SEARCH_DN=cn=admin,dc=vmware,dc=com \
LDAP_SEARCH_PWD=admin \
LDAP_BASE_DN=dc=vmware,dc=com \
LDAP_FILTER= \
LDAP_UID=cn \
LDAP_SCOPE=3 \
LDAP_TIMEOUT=5 \
EMAIL_HOST=smtp.vmware.com \
EMAIL_PORT=3306 \
EMAIL_USR= \
EMAIL_PWD= \
EMAIL_SSL=false \
EMAIL_FROM="admin<admin@harbor.com>" \
EMAIL_IDENTITY= \
REGISTRY_URL=127.0.0.1:5000 \
TOKEN_EXPIRATION=30 \
CFG_EXPIRATION=5 \
MAX_JOB_WORKERS=3 \
VERIFY_REMOTE_CERT=off \
PROJECT_CREATION_RESTRICTION=everyone \
HARBOR_ADMIN_PASSWORD=Harbor12345 \
ADMIRAL_URL="" \
WITH_NOTARY=false \
WITH_CLAIR=false \
UI_SECRET=$ui_secret \
JOBSERVICE_SECRET=$jobservice_secret \
JOBSERVICE_URL=http://jobservice \
PORT=$port JSON_CFG_STORE_PATH=$store KEY_PATH=$key $binary
