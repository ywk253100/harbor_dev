#!/bin/bash
set -e

# install kubectl
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
install kubectl /usr/local/bin/kubectl

# install minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
install minikube-linux-amd64 /usr/local/bin/minikube

# Kubernetes v1.18+ needs conntract to be installed on debian based machines
apt-get update
apt-get install conntrack -y

minikube start --driver=none --insecure-registry "0.0.0.0/0"