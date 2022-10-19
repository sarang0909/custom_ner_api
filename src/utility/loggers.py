"""
A module to configure and create logger.

"""


import logging
from logging import handlers
import os
from pathlib import Path
from src.utility.utils import config
from src.utility import constants

# If log path doesn't exist then create log file path
log_folder_path = Path(config.get(constants.LOG_FOLDER_PATH))
if not log_folder_path.exists():
    os.makedirs(log_folder_path)

# Define log file name
log_path = log_folder_path / config.get(constants.LOG_FILE_NAME)

# Define log file size and backup count
LOG_FILE_SIZE = int(config.get(constants.MAX_LOG_FILE_SIZE))
LOG_FILES_BACKUP_COUNT = int(config.get(constants.LOG_FILES_BACKUP_COUNT))

logger = logging.getLogger(str(config.get(constants.APP_NAME)))
logger.setLevel(logging.INFO)

# Define formatter and loghandler
formatter = logging.Formatter(str(config.get(constants.LOG_FORMATTER)))
loghandler = handlers.RotatingFileHandler(
    log_path, maxBytes=LOG_FILE_SIZE, backupCount=LOG_FILES_BACKUP_COUNT
)
loghandler.setLevel(logging.DEBUG)
loghandler.setFormatter(formatter)

logger.addHandler(loghandler)
