import os


def print_sub(dir_path):
    entries = os.scandir(dir_path)
    for object in entries:
        if object.is_dir():
            print(object.name)
            print_sub(object.path)


# program starts
path = os.getcwd()
print_sub(path)
