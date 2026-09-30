#!/bin/bash
set -e
kubectl apply -f <(cat templates/configmap.yaml.j2)
kubectl apply -f <(cat templates/deployment.yaml.j2)
kubectl apply -f <(cat templates/service.yaml.j2)
kubectl get pods
kubectl get svc
