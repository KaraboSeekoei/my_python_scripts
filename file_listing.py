from pathlib import Path

folder = Path(".")

def files_in_folder():
    for file in folder.iterdir():
        if file.is_file():
            print(file.name)

def list_files_by_ext(folder_path,ext_tuple):
    folder = Path(folder_path)
    for file in folder.iterdir():
        if file.is_file() and file.name.endswith(ext_tuple):
            print(file.name)
list_files_by_ext("BasicMath",".py")