
#!/bin/bash

TAG=`date +"%Y%m%d%H%M%S"`

echo "$TAG"

docker build -t infominer.azurecr.io/trainning2:v"$TAG" .

docker push infominer.azurecr.io/trainning2:v"$TAG"

docker build -f  Dockerfile_flag -t infominer.azurecr.io/trainning3:v"$TAG" .

docker push infominer.azurecr.io/trainning3:v"$TAG"

echo  "version=$TAG" > .env

sh up.sh
