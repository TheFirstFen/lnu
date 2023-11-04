import os


def print_sub(dir_path):
    dirs = os.scandir(dir_path)

    for d in dirs:
        if d.is_dir():
            print(d.name)
            print_sub(d.path)


path = os.getcwd()
print_sub(path)
