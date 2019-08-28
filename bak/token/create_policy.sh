#!/bin/bash

curl -X POST -k -i -H "Content-type:application/json" \
-H "x-xenon-auth-token: 6110f62b-162e-42b3-86b0-b92804c7f22d" \
-d '{"project_id":1, "target_id":1, "name":"policy01", "enabled": 0}' \
https://10.192.132.194/api/policies/replication
