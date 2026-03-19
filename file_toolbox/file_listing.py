from pathlib import Path
from datetime import datetime, date

# List all files in a folder
def files_in_folder(folder_path):
    folder = Path(folder_path)
    if not folder.is_dir():
        print(f"Error: {folder_path} is not a valid directory.")
        return
    for file in folder.iterdir():
        if file.is_file():
            print(file.name)

# List files by their extensions
def list_files_by_ext(folder_path, ext_tuple):
    folder = Path(folder_path)
    if not folder.is_dir():
        print(f"Error: {folder_path} is not a valid directory.")
        return
    for file in folder.iterdir():
        if file.is_file() and file.name.endswith(ext_tuple):
            print(file.name)

# List files with their modification dates
def files_by_date(folder_path, ext_tuple):
    folder = Path(folder_path)
    if not folder.is_dir():
        print(f"Error: {folder_path} is not a valid directory.")
        return
    for file in folder.iterdir():
        if file.is_file() and file.name.endswith(ext_tuple):
            mod_time = datetime.fromtimestamp(file.stat().st_mtime).date()
            print(f"{file.name} - {mod_time}")

# Allows the script to run directly or be imported
if __name__ == "__main__":
    # Example usage:
    folder = input("Enter the folder path: ")
    extensions = input("Enter file extensions (comma-separated, e.g. .py,.txt): ")

    # Convert user input into a tuple
    ext_tuple = tuple(ext.strip() for ext in extensions.split(","))

    files_by_date(folder, ext_tuple)