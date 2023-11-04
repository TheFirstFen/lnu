import os


def count_directories(dir_path):
    count = 0
    current_dir = os.scandir(dir_path)

    for entry in current_dir:
        if entry.is_dir():
            count += 1
    return count


def count_files(dir_path):
    count = 0
    current_dir = os.scandir(dir_path)
    for entry in current_dir:
        if entry.is_file():
            count += 1
    return count


dir_path = os.getcwd()
print(count_files(dir_path))
print(count_directories(dir_path))
