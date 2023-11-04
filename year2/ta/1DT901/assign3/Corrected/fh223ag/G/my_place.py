import os

dir_path = os.getcwd()
lst = os.scandir(dir_path)


# Function for number of directories
def count_directories(dir_path):
    lst = os.scandir(dir_path)
    n_of_dir = 0
    for i in lst:
        if i.is_dir():
            n_of_dir += 1
    return n_of_dir


# Function for number of files
def count_files(dir_path):
    lst = os.scandir(dir_path)
    n_of_files = 0
    for i in lst:
        if i.is_file():
            n_of_files += 1
    return n_of_files


# Variables for printing
n_of_dirs = count_directories(dir_path)
n_files = count_files(dir_path)


# Print results
print("I am right now at:", dir_path)
print(f"Below me i have {n_of_dirs} directories/folders")
print(f"This directory contains {n_files} files")
