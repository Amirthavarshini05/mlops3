# 14c - Ansible 3-role MLOps Server

Roles:
- common: Python 3.11, pip, git, Docker
- mlflow: MLflow systemd service on port 5000
- dvc: DVC with S3 support

Target:
EC2 from Question 13.

Edit inventory.ini with the EC2 public IP and SSH key.

Run:
ansible-playbook -i inventory.ini site.yml

Verify on EC2:
systemctl status docker
systemctl status mlflow
dvc --version

If MLflow must be reachable externally, add TCP 5000 to the EC2 security group.
The Q13 security group only specifies 22 and 8000.
