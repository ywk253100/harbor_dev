#!/bin/bash
set -e

source common.sh

clarity_image=vmware/harbor-clarity-ui-builder:1.3.0

docker run --rm -v $harbor/src:/harbor_src $clarity_image /bin/bash /entrypoint.sh
