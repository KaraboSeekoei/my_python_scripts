from pathlib import Path
from datetime import datetime, date

# List all files in a folder
def files_in_folder(folder_path):
    folder = Path(folder_path)
    for file in folder.iterdir():
        if file.is_file():
            print(file.name)

# List files by their extensions
def list_files_by_ext(folder_path, ext_tuple):
    folder = Path(folder_path)  # Remember: Path converts strings to objects so we can access their methods
    for file in folder.iterdir():
        if file.is_file() and file.name.endswith(ext_tuple):
            print(file.name)

# List files with their modification dates
def files_by_date(folder_path, ext_tuple):
    folder = Path(folder_path)
    from pathlib import Path
from datetime import datetime, date

# List files with their modification dates
def files_by_date(folder_path, ext_tuple):
    # Ask user for folder path if none provided
    if folder_path is None or folder_path.strip() == "":
        folder_path = input("Enter the directory path: ")
    
    folder = Path(folder_path)

    if not folder.is_dir():
        print(f"Error: {folder_path} is not a valid directory.")
        return  # Stop the function

    for file in folder.iterdir():
        if file.is_file() and file.name.endswith(ext_tuple):
            mod_time = datetime.fromtimestamp(file.stat().st_mtime).date()
            print(f"{file.name} - {mod_time}")

# Example usage
files_by_date("", ".py")  # Can replace with any folder and extension
# Or let user input folder path
# files_by_date(ext_tuple=".txt")  
# Example usage

