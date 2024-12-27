# dev_python_backup_folder

### Documentation for `dev_python_backup_folder`

#### Overview
This project provides a Docker container to backup a source folder to a target destination. The backup process is managed by a Python script that creates tar.gz archives of the specified source folder and stores them in the backup folder.

#### Prerequisites
- Docker installed on your system.
- Python 3 installed on your system.

#### Installation

1. **Install Python 3**:
    ```shell
    apt install python3
    ```

2. **Install Docker**:
    - Add Docker group:
        ```shell
        sudo groupadd docker
        ```
    - Add your user to the Docker group:
        ```shell
        sudo usermod -aG docker $USER
        ```
    - Verify Docker installation:
        ```shell
        docker run hello-world
        ```

#### Usage

1. **Build Docker Image**:
    ```shell
    ./docker-build.sh
    ```

2. **Run Docker Container**:
    ```shell
    ./docker-run.sh
    ```

3. **Access the Container**:
    - To bash into the running container:
        ```shell
        docker exec -it backup "bash"
        ```

#### Environment Variables

- `SOURCE_FOLDER`: The folder to be backed up.
- `BACKUP_FOLDER`: The folder where backups will be stored.
- `CRONTAB_STRING`: The crontab string to schedule backups.
- `TIMEZONE`: The timezone for the container.

#### Scripts

- **backup.py**: The main script that performs the backup.
- **docker-build.sh**: Script to build the Docker image.
- **docker-run.sh**: Script to run the Docker container.
- **docker-clean.sh**: Script to clean up Docker containers and images.
- **docker-rebuild.sh**: Script to clean and rebuild the Docker image.

#### Docker Workflow

The project includes a GitHub Actions workflow to build and push the Docker image to Docker Hub on every push to the `main` branch.

#### Example Crontab String

- `* * * * *`: Runs the backup every minute.

#### Notes

- Ensure the environment variables are set correctly before running the container.
- The default values for the environment variables can be overridden when running the container.

#### Troubleshooting

- If you encounter permission issues with Docker, ensure your user is added to the Docker group and restart your session.
- Check the logs for any errors during the backup process.


### misc

> docker container to backup source folder to target destination

```shell
apt install python3
```

```shell
sudo groupadd docker
sudo usermod -aG docker $USER
docker run hello-world
```

> bash into container

```
docker exec -it backup "bash"
```
