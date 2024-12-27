import os
import tarfile
import logging
import sys
import time
import os
import datetime
from crontab import CronTab


def backup_folder_func(source_folder, backup_folder):
    # Create backup folder if it doesn't exist
    os.makedirs(backup_folder, exist_ok=True)

    # Generate the backup file name with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_file = os.path.join(backup_folder, f"backup_{timestamp}.tar.gz")

    # Create tar.gz file
    with tarfile.open(backup_file, "w:gz") as tar:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                tar.add(file_path, arcname=os.path.relpath(file_path, source_folder))
                logging.info(f"{SCRIPT_NAME}: Added {file_path} to {backup_file}")

    logging.info(f"{SCRIPT_NAME}: Backup completed successfully: {backup_file}")


def parse_crontab_func(crontab_string):
    try:
        cron = CronTab(crontab_string)
        return cron
    except ValueError as e:
        logging.error(f"Invalid crontab string: {crontab_string}")
        raise e


def schedule_backup_func(source_folder, backup_folder):
    backup_folder_func(source_folder, backup_folder)


def set_env_func():
    # Set the environment variables
    # os.environ["SOURCE_FOLDER"] = "/source"
    # os.environ["BACKUP_FOLDER"] = "/backup"
    # os.environ["CRONTAB_STRING"] = "* * * * *"
    os.environ["TZ"] = os.getenv("TZ")
    time.tzset()  # Apply the change
    logging.info(f"TZ: {os.environ['TZ']}")


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    set_env_func()
    current_file_path = __file__
    # Get only the file name
    current_file_name = os.path.basename(current_file_path)
    SCRIPT_NAME = current_file_name

    logging.info(f"Current file path: {current_file_path}")
    logging.info(f"Current file name: {current_file_name}")
    logging.info(f"{SCRIPT_NAME}: Start")

    # Define the source folder and backup folder
    source_folder = os.getenv("SOURCE_FOLDER")
    backup_folder = os.getenv("BACKUP_FOLDER")

    if not source_folder or not backup_folder:
        logging.error(
            f"{SCRIPT_NAME}: SOURCE_FOLDER or backup_folder_func environment variable not defined."
        )
        sys.exit(1)

    logging.info(f"{SCRIPT_NAME}: Source folder: {source_folder}")
    logging.info(f"{SCRIPT_NAME}: Backup folder: {backup_folder}")

    # Define the crontab string
    CRONTAB_STRING = os.getenv(
        "CRONTAB_STRING", "* * * * *"
    )  # Default to run every hour
    logging.info(f"{SCRIPT_NAME}: Crontab string: {CRONTAB_STRING}")
    parse_crontab_func(CRONTAB_STRING)

    # Schedule the backup function
    schedule_backup_func(source_folder, backup_folder)

    logging.info(f"{SCRIPT_NAME}: Finish")

    # Keep the script running and check the schedule
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    while True:
        now = datetime.datetime.now()
        cron = CronTab(CRONTAB_STRING)
        if cron.test(now):  # Check if current time matches cron schedule
            logging.info(f"{SCRIPT_NAME}: cron job triggered at {now}")
            schedule_backup_func(source_folder, backup_folder)
            time.sleep(1)  # Prevent multiple triggers within the same minute
        else:
            logging.info(f"{SCRIPT_NAME}: sleeping at {now}")

        time.sleep(1)  # Avoid busy waiting
