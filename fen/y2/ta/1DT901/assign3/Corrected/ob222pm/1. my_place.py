import os


def count_directories(dir_path):
    dir_count = 0
    entries = os.scandir(dir_path)
    for object in entries:
        if object.is_dir():
            dir_count += 1
    return dir_count


def count_files(dir_path):
    file_count = 0
    entries = os.scandir(dir_path)
    for object in entries:
        if object.is_file():
            file_count += 1
    return file_count


# main program starts here
path = os.getcwd()
print("Current dir:", path)
print("Number of directories:", count_directories(path))
print("Number of files:", count_files(path))
