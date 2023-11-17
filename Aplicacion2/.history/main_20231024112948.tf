terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-east-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-053b0d53c279acc90"
  instance_type = "t2.micro"
  key_name = "appmovil"
  vpc_security_group_ids = [ "sg-0a64fe66b389fc4f3" ]
  associate_public_ip_address = true 
  provisioner "file" {
    source = "script.sh"
    destination = "/home/ubuntu/script.sh"
  }
  connection {
    type = "ssh"
    user = "ubuntu"
    private_key = "${file("./appmovil.pem")}"
    host = "${self.public_ip}"
  }

  tags = {
    Name = "EjemploClase"

  }
}
