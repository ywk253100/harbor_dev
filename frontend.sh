#!/bin/bash
set -e

source common.sh

clarity_image=vmware/harbor-clarity-ui-builder:1.4.1

docker run --rm -v $codes/src:/harbor_src $clarity_image /bin/bash /entrypoint.sh
