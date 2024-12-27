#/bin/bash
cat $0 && echo

# export SOURCE_FOLDER=".vscode"
export SOURCE_FOLDER="venv"
export BACKUP_FOLDER="backup-target"

docker run --name backup \
    -e SOURCE_FOLDER=/data/source \
    -e BACKUP_FOLDER=/data/backup \
    -e TZ="Australia/Melbourne" \
    -v ./${SOURCE_FOLDER}:/data/source \
    -v ./${BACKUP_FOLDER}:/data/backup \
    jdedev/backup:latest