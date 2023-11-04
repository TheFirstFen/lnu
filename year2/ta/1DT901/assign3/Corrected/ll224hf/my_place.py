import os


# Function to count the amount of directories inside current directory.
def count_dirs(path):
    no_dir = 1
    entries = os.scandir(path)
    for entry in entries:
        if entry.is_dir():
            no_dir += 1
    return no_dir


# Function to count the amount of files inside current directory.
def count_files(path):
    n_file = 0
    entries = os.scandir(path)
    for entry in entries:
        if entry.is_file():
            n_file += 1
    return n_file


"""
Main
"""

path = os.getcwd()
print(path)

n_fold = count_dirs(path)
n_files = count_files(path)

print(f"I am right now at: {path} \nBelow me I have" +
      f" {n_fold-1} directories/folders \n" +
      f"This directory contains {n_files} files")
