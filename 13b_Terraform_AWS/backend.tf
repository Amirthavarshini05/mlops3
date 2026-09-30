terraform {
  backend "s3" {
    bucket         = "REPLACE-WITH-EXISTING-TERRAFORM-STATE-BUCKET"
    key            = "mlops/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "REPLACE-WITH-EXISTING-TERRAFORM-LOCK-TABLE"
    encrypt        = true
  }
}
