import os


# Function for counting dirs
def count_directories(dir_path):
    dir_count = 0
    entries = os.scandir(dir_path)
    for e in entries:
        if e.is_dir():
            dir_count += 1
    return dir_count


# Function for counting files
def count_files(dir_path):
    files_count = 0
    entries = os.scandir(dir_path)
    for e in entries:
        if e.is_file():
            files_count += 1
    return files_count


# Program starts
path = os.getcwd()
print("I am right now at:", path)
count_dir = count_directories(path)
print(f"Below me I have {count_dir-1} directories/folders")
count_file = count_files(path)
print(f"This directory contains {count_file} files")
