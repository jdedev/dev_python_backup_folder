#bash
export SOURCE_FOLDER='app'
export BACKUP_FOLDER='backup'

docker run --name backup \
    -e SOURCE_FOLDER=${SOURCE_FOLDER} \
    -e BACKUP_FOLDER=${BACKUP_FOLDER} \
    # -v ${SOURCE_FOLDER}:/data/source \
    # -v ${BACKUP_FOLDER}:/data/backup \
    backup