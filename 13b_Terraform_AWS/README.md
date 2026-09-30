# 13b - Terraform AWS MLOps Infrastructure

Resources:
- EC2 t2.micro
- S3 bucket for ML models
- Security Group with only TCP 22 and 8000 ingress
- S3 backend + DynamoDB locking

IMPORTANT:
The backend S3 bucket and DynamoDB lock table must exist BEFORE `terraform init`.
Create them separately (AWS Console or a bootstrap Terraform project).

Commands:
terraform init
terraform validate
terraform plan
terraform apply
terraform output

Copy terraform.tfvars.example to terraform.tfvars and fill real values.

Security note:
0.0.0.0/0 is used for the lab requirement. In real deployments, restrict SSH to your IP.
