import os

path = os.getcwd()


def print_sub(dir_path):
    entries = os.scandir(dir_path)
    for e in entries:
        if e.is_dir():
            print(e.name)
            print_sub(e.path)
    return ''


print(print_sub(path))
