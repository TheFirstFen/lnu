import os


def count_directories(dir_path):
    dir_count = 0
    dirs = os.scandir(dir_path)
    for dir in dirs:
        if dir.is_dir():
            dir_count += 1
    print("Below me i have", dir_count, "directories/folders")


def count_files(dir_path):
    files_count = 0
    dirs = os.scandir(dir_path)
    for path in dirs:
        if path.is_file():
            files_count += 1
    print("This directory contains", files_count, "files")


# Program start
dir_path = os.getcwd()
print("I am right now at:", dir_path)
count_directories(dir_path)
count_files(dir_path)
