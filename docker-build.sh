#bash
docker build -t backup .
docker tag backup jdedev/backup:latest
docker push jdedev/backup:latest
docker image ls