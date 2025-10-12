import os
from modules.sorter import FileSorter
from modules.logger import setup_logger
from modules.error_handler import DirectoryErrorHandler

def main():
    # Initialize logger
    logger = setup_logger()
    logger.info("Logger initialized successfully.")
    
    # Define the directory to organize
    directory_to_organize = input("Enter the path of the directory to organize: ").strip()
    
    # Handle directory errors
    if not DirectoryErrorHandler.validate_directory(directory_to_organize):
        logger.error(f"Invalid directory: {directory_to_organize}")
        return
    
    # Organize files
    sorter = FileSorter(directory_to_organize, logger)
    sorter.organize_files()

if __name__ == "__main__":
    main()
