#bash
sudo rm -rf backup-target
sudo rm -rf source
sudo rm -rf backup

docker rm -vf $(docker ps -aq)
docker ps -a
docker rmi -f $(docker images -aq)
docker image ls