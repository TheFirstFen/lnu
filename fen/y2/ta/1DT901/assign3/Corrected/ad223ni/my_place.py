import os


def count_directories(dir_path):
    count = 0
    for entry in os.scandir(dir_path):
        if entry.is_dir():
            count += 1
    return count


def count_files(dir_path):
    count = 0
    for entry in os.scandir(dir_path):
        if entry.is_file():
            count += 1
    return count


current_dir = os.getcwd()
print("I am right now at:", current_dir)

num_directories = count_directories(current_dir)
print("Below me I have", num_directories, "directories/folders")

num_files = count_files(current_dir)
print("This directory contains", num_files, "files")
