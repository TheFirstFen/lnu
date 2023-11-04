import os


def count_directories(dir_path):
    directory_count = 0
    for name in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, name)):
            directory_count += 1
    return directory_count


def count_file(dir_path):
    file_count = 0
    for name in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, name)):
            file_count += 1
    return file_count


path = os.getcwd()
print("I am right now at:", path)
dir_count = count_directories(path)
print(f"Below me I have {dir_count} directories/folders")
file_count = count_file(path)
print(f"This directory contains {file_count} files")
