variable "project_name" {
  type        = string
  description = "Name of project, used to build resource names"
  default     = "panda01"
}

variable "region" {
  type        = string
  description = "AWS Region for deployment"
  default     = "eu-west-1"
}
