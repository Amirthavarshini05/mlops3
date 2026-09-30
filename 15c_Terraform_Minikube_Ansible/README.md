# 15c - Terraform Kubernetes + Ansible ML Stack

The lab allows EKS or Minikube. This folder uses Minikube because it is much easier for a local practical exam.

Terraform creates a Minikube cluster.
Ansible deploys:
- ConfigMap
- Deployment with 2 FastAPI replicas
- Service on port 8000

End-to-end:
terraform apply
ansible-playbook
kubectl get pods
curl /predict

Prerequisites:
- Docker
- Minikube
- kubectl
- Terraform
- Ansible (Linux/WSL recommended)

For the FastAPI image, build it locally:
docker build -t fastapi-ml-exp10 ../10b

For Minikube:
minikube image load fastapi-ml-exp10

Then update the deployment image if needed.
