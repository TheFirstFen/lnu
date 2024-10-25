import os
path = os.getcwd()


def count_directories(path):
    counter = 0
    for i in os.scandir(path):
        if i.is_dir():
            counter += 1
    return counter


def count_files(path):
    counter = 0
    for i in os.scandir(path):
        if i.is_file():                # Checks if item is a file
            counter += 1               # Returns the number of files
    return counter


print("I am here", path)
print(f"Below me i have {count_directories(path)} folders")
print(f"This directory {count_files(path)} files")
