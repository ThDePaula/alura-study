resource "aws_security_group" "acesso_ssh_us-east-2" {
  name = "acesso_ssh_us-east-2"
  description = "Acesso via ssh"

  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = "${var.cdirs_acesso_remoto}"
  }

  tags = {
    Name = "ssh"
  }
}

resource "aws_security_group" "acesso_ssh_us-east-1" {
  provider = "aws.us-east-1"
  name = "acesso_ssh_us-east-1"
  description = "Acesso via ssh"

  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = "${var.cdirs_acesso_remoto}"
  }

  tags = {
    Name = "ssh"
  }
}