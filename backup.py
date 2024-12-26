import os
import tarfile
import datetime
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def backup_folder_func(source_folder, backup_folder):
    # Create backup folder if it doesn't exist
    os.makedirs(backup_folder, exist_ok=True)
    
    # Generate the backup file name with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_file = os.path.join(backup_folder, f"{timestamp}_backup.tar.gz")
    
    # Create tar.gz file
    with tarfile.open(backup_file, "w:gz") as tar:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                tar.add(file_path, arcname=os.path.relpath(file_path, source_folder))
                logging.info(f"Added {file_path} to {backup_file}")

    logging.info(f"Backup completed successfully: {backup_file}")

if __name__ == "__main__":
    logging.info('Start')

    # Define the source folder and backup folder
    source_folder = os.getenv("SOURCE_FOLDER")
    backup_folder = os.getenv("BACKUP_FOLDER")

    if not source_folder or not backup_folder:
        logging.error("SOURCE_FOLDER or BACKUP_FOLDER environment variable not defined.")
        sys.exit(1)

    logging.info(f"Source folder: {source_folder}")
    logging.info(f"Backup folder: {backup_folder}")

    backup_folder_func(source_folder, backup_folder)
    
    logging.info('Finish')

    # Run the tree command and log its output
    # try:
    #     result = subprocess.run(['tree', source_folder], capture_output=True, text=True, check=True)
    #     logging.info(f"Tree command output:\n{result.stdout}")
    # except subprocess.CalledProcessError as e:
    #     logging.error(f"Tree command failed with error: {e}")

    # Keep the script running
    # while True:
    #     time.sleep(60)
    #     logging.info('Sleeping for 60 seconds...')

