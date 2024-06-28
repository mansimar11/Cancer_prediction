import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath, mode='a'),  # 'a' for append mode
        logging.StreamHandler(sys.stdout)
    ]
)

# Set the logger level explicitly
logger = logging.getLogger("cancerpredlogger")
logger.setLevel(logging.INFO)

# Example usage of the logger
logger.info("Logging started successfully.")
