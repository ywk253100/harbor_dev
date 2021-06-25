#!/bin/bash

docker run -it --privileged -v /Users/yinw/workspace/src/github.com/goharbor/harbor:/drone \
    -v $(pwd)/config/nginx/server.crt:/ca/harbor_ca.crt -w /drone harbor-repo.vmware.com/harbor-ci/goharbor/harbor-e2e-engine:3.0.1-ui \
    robot --exclude proxy_cache -v DOCKER_USER:ywk253100 -v DOCKER_PWD:$1 -v ip:$2 -v ip1: \
    -v http_get_ca:false \
    -v HARBOR_PASSWORD:Harbor12345 /drone/tests/robot-cases/Group1-Nightly/Setup.robot \
    /drone/tests/robot-cases/Group1-Nightly/Common.robot



