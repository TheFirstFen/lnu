import os


def pretty_print(dir_path, depth=0):
    dirs = os.scandir(dir_path)
    for dir in dirs:
        if dir.is_dir():
            print(" " * depth + dir.name)
            pretty_print(dir.path, depth + 2)


# Program start
dir_path = os.getcwd()
pretty_print(dir_path)
