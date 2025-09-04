import logger
import os
import sys
from datetime import datetime

LOG_FILE_NAME = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs",filename = LOG_FILE_NAME)
os.makedirs(logs_path, exist_ok=True)
log_file_path = os.path.join(logs_path, LOG_FILE_NAME)

import logging
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def get_logger():
    return logging

logger = get_logger()
logger.info("Logger has been set up.")

if __name__ == '__main__':
    logger.info("This is a test log message.")

# ...existing code...
# --- IGNORE ---
