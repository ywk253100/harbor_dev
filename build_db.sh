#!/bin/bash
set -e

source common.sh
cd $harbor
make -f $harbor/make/photon/Makefile _build_db -e VERSIONTAG=dev -e MARIADBVERSION=dev
