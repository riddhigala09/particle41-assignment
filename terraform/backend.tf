terraform {
  backend "s3" {
    bucket         = "simple-time-service-terraform-state"
    key            = "ecs/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "simple-time-service-terraform-locks"
    encrypt        = true
  }
}