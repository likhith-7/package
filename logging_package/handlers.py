import os
from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGS_DIR = os.getenv('CUSTOM_LOGS_DIR')

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

class LevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno <= self.level


class DateRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename, *args, **kwargs):
        today = datetime.now().strftime('%Y-%m-%d')
        log_folder = os.path.join(LOGS_DIR, today)
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)
        filename = os.path.join(log_folder, filename)
        super().__init__(filename, *args, **kwargs)

def cleanup_old_log_folders():
    log_folders = sorted(os.listdir(LOGS_DIR))
    if len(log_folders) > 5:
        folders_to_delete = log_folders[:-5]  # Keep the 5 most recent folders
        for folder in folders_to_delete:
            folder_path = os.path.join(LOGS_DIR, folder)
            if os.path.isdir(folder_path):
                try:
                    # Delete the contents within the folder before removing it
                    for root, dirs, files in os.walk(folder_path):
                        for file in files:
                            os.remove(os.path.join(root, file))
                    os.rmdir(folder_path)  # Remove the directory
                except OSError as e:
                    print(f"Error while deleting folder {folder_path}: {e}")

cleanup_old_log_folders()
