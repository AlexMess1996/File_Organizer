# File Organizer Script

A lightweight Python automation tool that organizes cluttered directories by categorizing files into structured folders based on their types (e.g., images, documents, audio).  
This project was developed to enhance productivity by automating tedious manual sorting and keeping directories clean and organized.

---

## Features

- **Automatic File Categorization** – Sorts files into predefined folders like `Images` and `Documents` using regular expressions.  
- **Modular Architecture** – Clean separation of responsibilities through dedicated modules for sorting, configuration, logging, and error handling.  
- **Dynamic File Types** – Add or modify file categories in `config.py` without changing the core logic.  
- **Robust Error Handling** – Validates paths and permissions and provides clear error feedback.  
- **Detailed Logging** – Logs all operations to both the console and a `.log` file for easier debugging and auditing.

---

## Tech Stack

- **Language:** Python 3  
- **Libraries:** `os`, `shutil`, `re`, `logging`  
- **Architecture:** Modular (Main, Sorter, Config, Logger, Error Handler)

---

## Project Structure

```
file-organizer/
│
├── main.py                      # Entry point – initializes logger, validates directory, runs sorter
├── modules/                      # All core functionality lives here
│   ├── sorter.py                 # Handles file categorization and movement
│   ├── config.py                 # Stores file category patterns (regex)
│   ├── logger.py                 # Configures logging
│   └── error_handler.py          # Manages validation and errors
│
├── logs/
│   └── file_organizer.log        # Log file with history of operations
│
├── tests/                        # (Optional) Unit tests for modules
│
├── .gitignore                    # Git ignore file
├── LICENSE                       # License file (MIT)
├── requirements.txt              # Project dependencies (if any)
└── README.md                     # Project documentation
```

---

## How It Works

1. **Run `main.py`** and provide the path to the directory you want to organize.  
2. The script validates the directory using `error_handler.py`.  
3. Files are categorized based on regex patterns in `config.py`.  
4. `sorter.py` moves files into the corresponding folders.  
5. All actions are logged through `logger.py` to both console and file.

Example of file type configuration:
```python
FILE_CATEGORIES = {
    "Images": r".(jpg|jpeg|png|gif|bmp)$",
    "Documents": r".(pdf|docx?|txt|xls[xm]?)$"
}
```

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/file-organizer.git

# Navigate into the project
cd file-organizer

# (Optional) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# Install dependencies (standard library is used, no extra requirements)
```

---

## Usage

```bash
# Run the script
python main.py /path/to/your/directory
```

After running, your files will be sorted into categorized folders automatically.

---

## Logging

All operations are:
- Displayed on the **console** in real time  
- Stored in a log file inside the `logs/` directory for future reference

---

## Future Improvements

- Recursive support for nested directories  
- Graphical User Interface (GUI) for non-CLI users  
- ⚙️ Dynamic configuration through external files or CLI

---

## 📚 References

- [Python `os` Documentation](https://docs.python.org/3/library/os.html)  
- [Python `shutil` Documentation](https://docs.python.org/3/library/shutil.html)  
- [Python `re` Documentation](https://docs.python.org/3/library/re.html)  
- [Python `logging` Documentation](https://docs.python.org/3/library/logging.html)

---

## 👤 Author

**Alexandros Messaritakis**  
💻 Data Scientist & Developer

[![GitHub](https://img.shields.io/badge/GitHub-000?style=flat&logo=github&logoColor=white)](https://github.com/AlexMess1996)
