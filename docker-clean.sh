#bash
docker rm -vf $(docker ps -aq)
docker ps -a
docker rmi -f $(docker images -aq)
docker image ls