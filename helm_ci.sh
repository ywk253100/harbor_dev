#!/bin/bash
set -e 

chart_dir=./contrib/helm/harbor
domain=harbor.10.170.95.169.xip.io
port=32700

release_name=harbor-for-ci
tag=dev

# clean
echo "Cleaning environment..."
helm delete --purge $release_name || true
status=""
for (( i=0; i<30; i++ ))
do
	pending_pods="$(kubectl get pods 2>/dev/null | grep $release_name)" || true
    if [ -z "${pending_pods}" ]
    then
    	status="ok"
    	break
    fi
    echo "Pods still running, wait for 10 seconds..."
    sleep 10s
done

if [ $status != "ok" ]
then
	echo "Timeout for cleaning environment"
    exit 1
else
	echo "Pods are cleaned up successfully"
fi



# download the dependencies
echo "Downloading dependencies..."
helm dependency update $chart_dir

# install
echo "Installing Harbor..."

params="persistence.enabled=false,externalDomain=$domain,externalPort=$port,\
adminserver.image.tag=$tag,adminserver.image.pullPolicy=Always,\
jobservice.image.tag=$tag,jobservice.image.pullPolicy=Always,\
ui.image.tag=$tag,ui.image.pullPolicy=Always,\
database.internal.image.tag=$tag,database.internal.image.pullPolicy=Always,\
registry.image.tag=$tag,registry.image.pullPolicy=Always,\
clair.image.tag=$tag,clair.image.pullPolicy=Always,\
notary.server.image.tag=$tag,notary.server.image.pullPolicy=Always,\
notary.signer.image.tag=$tag,notary.signer.image.pullPolicy=Always"

helm install --debug --name $release_name --set $params $chart_dir

# check the status of installation
status=""
for (( i=0; i<30; i++ ))
do
	code=$(curl -s -k -o /dev/null -w "%{http_code}" https://$domain:$port)
    if [ $code -eq 200 ]
    then
    	status="ok"
    	break
    fi
    echo "Test connection failed, wait for 10 seconds..."
    sleep 10s
done

if [ $status != "ok" ]
then
	echo "Timeout for testing connection"
    exit 1
else
	echo "Harbor is setup successfully"
fi
