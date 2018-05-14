#!/bin/bash
set -e

source ./common.sh

binary=$codes/src/adminserver/adminserver

LOG_LEVEL=$log_level \
EXT_ENDPOINT=http://$local_host_ip \
AUTH_MODE=db_auth \
SELF_REGISTRATION=on \
POSTGRESQL_HOST=$database_host \
POSTGRESQL_PORT=$database_port \
POSTGRESQL_USERNAME=$database_username \
POSTGRESQL_PASSWORD=$database_password \
POSTGRESQL_DATABASE=$database_registry \
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
REGISTRY_URL=$registry \
TOKEN_EXPIRATION=30 \
CFG_EXPIRATION=5 \
MAX_JOB_WORKERS=3 \
VERIFY_REMOTE_CERT=off \
PROJECT_CREATION_RESTRICTION=everyone \
HARBOR_ADMIN_PASSWORD=Harbor12345 \
ADMIRAL_URL="" \
WITH_NOTARY=false \
WITH_CLAIR=true \
CLAIR_DB_HOST=$database_host \
CLAIR_DB_PORT=$database_port \
CLAIR_DB_USERNAME=$database_username \
CLAIR_DB_PASSWORD=$database_password \
CLAIR_DB=$database_clair \
UI_SECRET=$ui_secret \
JOBSERVICE_SECRET=$jobservice_secret \
JOBSERVICE_URL=http://jobservice \
PORT=$adminserver_port KEY_PATH=$encrypt_key $binary
