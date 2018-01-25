#!/bin/bash

url=$1
curl -X POST -k -i -H "Content-type:application/x-www-form-urlencoded" \
--data-urlencode "CastleAuthorization=Basic YWRtaW5pc3RyYXRvckB2c3BoZXJlLmxvY2FsOkFkbWluITIz" \
"$url"
