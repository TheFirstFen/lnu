# my_place.py
#
# Author: Samuel Berg
# Date: 03-Oct-2022

import os
'''count_directories(dir_path):
Counts all the directories directly below
current directory for the given path.
'''


def count_directories(dir_path):  # Returns the number of directories
    folders = 0
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir():
            folders += 1
    return folders


'''count_files(dir_path):
Counts all the files directly below
current directory for the given path.
'''


def count_files(dir_path):  # Returns the number of files
    files = 0
    for _, _, filenames in os.walk(dir_path):
        files += len(filenames)
        return files


# Main code
path = os.getcwd()

# Prints the results
print(f'I am right now at: {path}')
print(f'Below me I have {count_directories(path)} directories/folders')
print(f'This directory contains {count_files(path)} files')
