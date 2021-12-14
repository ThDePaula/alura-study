provider "aws" {
  region = "us-east-2"
}

resource "aws_instance" "dev" {
  count = 3  
  ami = "ami-03a0c45ebc70f98ea"
  instance_type = "t2.micro"
  key_name = "terraform-aws"
 
  tags = {
      Name = "dev${count.index}"
  }

  vpc_security_group_ids = ["${aws_security_group.acesso_ssh.id}"]
}

resource "aws_instance" "dev4" {
  ami = "ami-03a0c45ebc70f98ea"
  instance_type = "t2.micro"
  key_name = "terraform-aws"
  
  tags = {
      Name = "dev4"
  }

  vpc_security_group_ids = ["${aws_security_group.acesso_ssh.id}"]
  depends_on = [aws_s3_bucket.dev4]
}

resource "aws_instance" "dev5" {
  ami = "ami-03a0c45ebc70f98ea"
  instance_type = "t2.micro"
  key_name = "terraform-aws"
  
  tags = {
      Name = "dev5"
  }

  vpc_security_group_ids = ["${aws_security_group.acesso_ssh.id}"]
}

resource "aws_security_group" "acesso_ssh" {
  name = "acesso_ssh"
  description = "Acesso via ssh"

  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["177.195.68.228/32"]
  }

  tags = {
    Name = "ssh"
  }
}

resource "aws_s3_bucket" "dev4" {
  bucket = "thiagolabs-dev4"
  acl = "private"

  tags = {
    Name = "thiagolabs-dev4"
  }
}