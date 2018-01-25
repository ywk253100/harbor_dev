#!/bin/bash

curl -X POST -k -i -H "Content-type:application/json" \
-H "x-xenon-auth-token: 6110f62b-162e-42b3-86b0-b92804c7f22d" \
-d '{"name":"project01", "description":"This is the coolest project", "isPublic": true}' \
https://10.192.132.194:8282/projects
