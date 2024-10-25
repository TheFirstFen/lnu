import os


def print_sub(dir_path):
    dir_list = os.scandir(dir_path)
    for path in dir_list:
        if path.is_dir():
            print(path.name)
            new_path = os.path.join(dir_path, path.name)
            print_sub(new_path)


print_sub(os.getcwd())
