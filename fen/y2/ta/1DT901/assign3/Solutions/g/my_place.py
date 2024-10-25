import os


def count_directories(dir_path):  # Returns the number of directories
    count = 0
    dirs = os.scandir(dir_path)

    for d in dirs:
        if d.is_dir():
            count += 1

    return count


def count_files(dir_path):  # Returns the number of files
    counter = 0
    dirfiles = os.scandir(dir_path)

    for f in dirfiles:
        if f.is_file():
            counter += 1

    return counter


path = os.getcwd()
print('I am right now at:', path)
print('Below me I have', count_directories(path), 'directories/folders')
print('This directory contains', count_files(path), 'files')
