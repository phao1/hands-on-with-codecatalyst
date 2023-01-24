provider "aws" {
    region = "eu-west-1"
    default_tags {
        tags = {
            Project = "DevOps PlayGround Jan 2023"
        }
    }
}

terraform {
  backend "s3" {
    bucket         = "299878581976-eu-west-1-terraform-state"
    key            = "devops-playground.tfstate"
    region         = "eu-west-1"
  }
}