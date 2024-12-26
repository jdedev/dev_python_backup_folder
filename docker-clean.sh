#bash
docker rm -vf $(docker ps -aq) && docker rmi -f $(docker images -aq)
docker build -t backup .
docker image ls