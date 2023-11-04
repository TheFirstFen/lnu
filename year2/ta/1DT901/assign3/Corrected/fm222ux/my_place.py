# Import OS module
import os


# Function for counting directory and files in path
def count_directory(path):
    entries = os.scandir()
    dir_count = 0
    file_count = 0
    for item in entries:
        if item.is_dir():
            dir_count += 1
        elif item.is_file():
            file_count += 1
    return dir_count, file_count


# Get current working directory
path = os.getcwd()

# Get directory number and file number
dir_count, file_count = count_directory(path)

# Result
print(f"I am right now at: {path}")
print(f"Below me I have {dir_count-1} directories/folders")
print(f"This directory contains {file_count} files")
