import os


def print_sub(dir_path):
    dirs = os.scandir(dir_path)
    for dir in dirs:
        if dir.is_dir():
            print(dir.name)
            print_sub(dir.path)


# Program start
dir_path = os.getcwd()
print_sub(dir_path)
