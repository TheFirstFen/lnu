import os


# Make functions

def count_directories(dir_path):
    dir_count = 0
    entries = os.scandir(dir_path)
    for obj in entries:
        if obj.is_dir():  # Is directory
            dir_count += 1
    return dir_count


def count_files(dir_path):
    file_count = 0
    entries = os.scandir(dir_path)
    for obj in entries:
        if obj.is_file():  # Is file
            file_count += 1
    return file_count


# Start program

path = os.getcwd()  # Get current
print("Current dir:", path)
print("Number of directories:", count_directories(path))
print("Number of files in directory;", count_files(path))
