variable "amis" {
  type = map

  default = {
      "us-east-2" = "ami-03a0c45ebc70f98ea"
      "us-east-1" = "ami-0e472ba40eb589f49"
  }
}

variable "cdirs_acesso_remoto" {
  type = list

  default = ["177.195.68.228/32","177.195.68.229/32"]
}

variable "key_name" {
  default = "terraform-aws"
}