import os

class DirectoryErrorHandler:
    @staticmethod
    def validate_directory(directory):
        if not os.path.exists(directory):
            print(f"Error: Directory {directory} does not exist.")
            return False
        if not os.access(directory, os.W_OK):
            print(f"Error: No write permissions for {directory}.")
            return False
        return True
 
