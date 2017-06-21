#!/bin/bash
set -e

source common.sh

clarity_image=vmware/harbor-clarity-ui-builder:1.1.2
static=$harbor/src/ui/static
ui_ng=$harbor/src/ui_ng/src

docker run --rm -v $static:/harbor_ui/dist -v $ui_ng:/harbor_ui/src \
$clarity_image /bin/bash /entrypoint.sh
