import os

# This gets the current working directory
current_directory = os.getcwd()
print("The current directory is: ", current_directory)


def count_directories(dir_path):
    dir_counter = 0
    for folder in os.listdir(dir_path):
        # Checks if the folder is a directory
        if os.path.isdir(folder):
            dir_counter += 1
    return f"There are {dir_counter} directories in this directory "


def count_files(dir_path):
    dir_counter = 0
    for file in os.listdir(dir_path):
        # Checks if the item is a file
        if os.path.isfile(file):
            dir_counter += 1
    return f"This directory contains {dir_counter} files"


directories = (count_directories(current_directory))
files = (count_files(current_directory))
print(directories, "\n", files)
