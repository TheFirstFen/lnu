import os


# Displays directory path and how many directories in current directory
def count_directories(dir_path):
    path = os.getcwd()
    asv = 0
    print("Current dir:", path)
    lst = os.scandir(path)
    for e in lst:
        if e.is_dir():
            asv += 1
    print(f"Below me I have {asv} directories/folders")


# Displayes the number of files in current directory
def count_files(dir_path):
    path = os.getcwd()
    entries = os.scandir(path)
    svd = 0
    for e in entries:
        if e.is_file():
            svd += 1
            print(f"This directory contains {svd} files")


# Calls the two previous functions
count_directories("")
count_files("")
