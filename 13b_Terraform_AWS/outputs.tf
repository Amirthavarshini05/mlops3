output "ec2_instance_id" {
  value = aws_instance.mlops_server.id
}

output "ec2_public_ip" {
  value = aws_instance.mlops_server.public_ip
}

output "ec2_public_dns" {
  value = aws_instance.mlops_server.public_dns
}

output "s3_bucket_name" {
  value = aws_s3_bucket.ml_models.bucket
}

output "security_group_id" {
  value = aws_security_group.mlops_sg.id
}
