import os
import tarfile
import datetime
import logging
import sys
import time
import os
import schedule
from crontab import CronTab  # type: ignore


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
    cron = CronTab(crontab_string)
    return cron


def schedule_backup_func(crontab_string, source_folder, backup_folder):
    cron = parse_crontab_func(crontab_string)
    schedule.every(cron.minute).minutes.do(
        backup_folder_func, source_folder, backup_folder
    )
    schedule.every(cron.hour).hours.do(backup_folder_func, source_folder, backup_folder)
    schedule.every(cron.day).days.do(backup_folder_func, source_folder, backup_folder)
    schedule.every(cron.month).months.do(
        backup_folder_func, source_folder, backup_folder
    )
    schedule.every(cron.dow).days.do(backup_folder_func, source_folder, backup_folder)


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    current_file_path = __file__
    # Get only the file name
    current_file_name = os.path.basename(current_file_path)
    SCRIPT_NAME = current_file_name

    print(f"Current file path: {current_file_path}")
    print(f"Current file name: {current_file_name}")
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
    crontab_string = os.getenv(
        "CRONTAB_STRING", "* * * * *"
    )  # Default to run every hour
    logging.info(f"{SCRIPT_NAME}: Crontab string: {crontab_string}")

    # Schedule the backup function
    schedule_backup_func(crontab_string, source_folder, backup_folder)

    logging.info(f"{SCRIPT_NAME}: Finish")

    # Keep the script running and check the schedule
    while True:
        schedule.run_pending()
        time.sleep(1)
