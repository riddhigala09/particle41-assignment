variable "aws_region" {
  type    = string
  default = "ap-south-1"
}

variable "container_image_url" {
  type = string
  description = "ECR or DockerHub image URL"
}
