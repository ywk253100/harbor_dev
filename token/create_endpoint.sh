#!/bin/bash

curl -X POST -k -i -H "Content-type:application/json" \
-H "x-xenon-auth-token: 6110f62b-162e-42b3-86b0-b92804c7f22d" \
-d '{"endpoint":"http://127.0.0.1", "name":"endpoint01", "username":"admin", "password":"Harbor12345", "insecure": true}' \
https://10.192.132.194/api/targets
