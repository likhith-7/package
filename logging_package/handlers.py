import os
from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGS_DIR = 'C:\\Users\\Likhith.gowda\\Desktop\\logsss'

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
    LOGS_DIR = 'C:\\Users\\Likhith.gowda\\Desktop\\logsss'  # Update with your directory path
    log_folders = sorted(os.listdir(LOGS_DIR))
    
    if len(log_folders) > 5:
        folders_to_delete = log_folders[:-5]  # Keep the 5 most recent folders
        
        for folder in folders_to_delete:
            folder_path = os.path.join(LOGS_DIR, folder)
            
            try:
                shutil.rmtree(folder_path)  # Remove the directory and its contents forcefully
            except Exception as e:
                print(f"Error while deleting folder {folder_path}: {e}")

cleanup_old_log_folders()
