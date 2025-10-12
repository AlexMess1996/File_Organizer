import logging
import os

def setup_logger():
   
    log_dir = os.path.join("logs")
    os.makedirs(log_dir, exist_ok=True)

    # Path to the log file
    log_file = os.path.join(log_dir, "file_organizer.log")

    # Create or get the logger instance
    logger = logging.getLogger("FileOrganizer")
    logger.setLevel(logging.DEBUG)  

    # Avoid duplicate log handlers
    if not logger.handlers:
        # File handler for saving logs to a file
        file_handler = logging.FileHandler(log_file, mode='a')  # 'a' to append to existing logs
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # Console handler for displaying logs in the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger
