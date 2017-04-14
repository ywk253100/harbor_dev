#!/bin/bash
set -e

source common.sh

clarity_image=vmware/harbor-clarity-ui-builder:0.8.4
static=$harbor/src/ui/static
ui_ng=$harbor/src/ui_ng/src

docker run --rm -v $static:/clarity-seed/dist -v $ui_ng:/clarity-seed/src \
$clarity_image /bin/bash /entrypoint.sh
