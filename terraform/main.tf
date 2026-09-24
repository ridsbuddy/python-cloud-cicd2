terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region = "eu-north-1"
}


resource "aws_instance" "app_server" {
  ami           = "ami-0c1ac8a41498c1a9c"
  instance_type = "t3.micro"

  tags = {
    Name = "python-cloud-cicd"
  }
}
