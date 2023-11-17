#!/bin/bash

apt update
apt install docker-compose -y

docker build -t micro1:v1.0 ./ms1/
docker build -t micro2:v1.0 ./ms2/
docker-compose up -d
