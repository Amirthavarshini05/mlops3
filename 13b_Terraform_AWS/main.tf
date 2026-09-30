terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_security_group" "mlops_sg" {
  name        = "mlops-security-group"
  description = "Allow SSH and FastAPI"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "MLOps-Security-Group"
  }
}

resource "aws_instance" "mlops_server" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.mlops_sg.id]

  tags = {
    Name = "MLOps-EC2"
  }
}

resource "aws_s3_bucket" "ml_models" {
  bucket = var.model_bucket_name

  tags = {
    Name = "ML Models"
  }
}
