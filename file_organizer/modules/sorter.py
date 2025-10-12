import os
import shutil
import re
from modules.config import FILE_CATEGORIES

class FileSorter:
    def __init__(self, directory, logger):
        self.directory = directory
        self.logger = logger

    def organize_files(self):
        for filename in os.listdir(self.directory):
            filepath = os.path.join(self.directory, filename)
            if os.path.isfile(filepath):
                category = self._determine_category(filename)
                if category:
                    self._move_file(filepath, category)
                else:
                    self.logger.warning(f"Uncategorized file: {filename}")
            else:
                self.logger.info(f"Skipping directory: {filename}")

    def _determine_category(self, filename):
        for category, pattern in FILE_CATEGORIES.items():
            if re.search(pattern, filename, re.IGNORECASE):
                return category
        return None

    def _move_file(self, filepath, category):
        dest_dir = os.path.join(self.directory, "organized", category)
        os.makedirs(dest_dir, exist_ok=True)
        shutil.move(filepath, os.path.join(dest_dir, os.path.basename(filepath)))
        self.logger.info(f"Moved {os.path.basename(filepath)} to {dest_dir}")
