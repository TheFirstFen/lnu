import os


def print_files(dir_path):
    dirs = os.scandir(dir_path)     # returns a list of all dirs in that path
    for path in dirs:
        if path.is_dir():
            next_path = os.path.join(dir_path, path.name)
            print_files(next_path)
        if path.is_file():
            print(path.name)


print_files(os.getcwd())
