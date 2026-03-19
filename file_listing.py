from pathlib import Path
from datetime import datetime, date

def files_in_folder(folder_path):
    folder = Path(folder_path)
    for file in folder.iterdir():
        if file.is_file():
            print(file.name)

def list_files_by_ext(folder_path,ext_tuple):
    folder = Path(folder_path) #Remember Path converts strings to objects so that we can access them
    for file in folder.iterdir():
        if file.is_file() and file.name.endswith(ext_tuple):
            print(file.name)

def files_by_date(folder_path, ext_tuple):
    folder =  Path(folder_path)
    for file in folder.iterdir():
        if file.is_file() and file.name.endswith(ext_tuple):
            mod_time = datetime.fromtimestamp(file.stat().st_mtime).date()
            print(f"{file.name } - {mod_time}")
files_by_date("BasicMath", ".py")



# list_files_by_ext("BasicMath",".py")