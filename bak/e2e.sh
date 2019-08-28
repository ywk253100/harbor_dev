#!/bin/bash
set -e

source common.sh

caDir=/tmp
engine=vmware/harbor-e2e-engine:1.38
harborEndpoint=harbor.10.170.95.169.xip.io:32700
notaryServerEndpoint=notary-harbor.10.170.95.169.xip.io:32700
harborEndpoint2=
harborAdminPassword=Harbor12345

docker run -i --privileged -v $codes:/drone -v $caDir:/ca -w /drone $engine \
pybot -v ip:$harborEndpoint -v notaryServerEndpoint:$notaryServerEndpoint \
-v ip1:$harborEndpoint2 -v HARBOR_PASSWORD:$harborAdminPassword \
/drone/tests/robot-cases/Group11-Nightly/Setup.robot \
/drone/tests/robot-cases/Group11-Nightly/mycase.robot
