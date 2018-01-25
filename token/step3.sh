#!/bin/bash

SAMLResponse=$1
curl -X POST -k -i -H "Content-type:application/x-www-form-urlencoded" \
--data-urlencode "RelayState=SessionId" \
--data-urlencode "SAMLResponse=$SAMLResponse" \
"https://10.192.132.194:8282/auth/psc/callback/token"
