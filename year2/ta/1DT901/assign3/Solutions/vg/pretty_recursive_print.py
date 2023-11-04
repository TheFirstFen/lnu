import os


def pretty_print(dir_path, depth):
    # global depth

    dirs = os.scandir(dir_path)

    for d in dirs:
        if d.is_dir():
            print(depth * '  ', d.name)
            depth += 1
            pretty_print(d.path, depth)
            depth -= 1


path = os.getcwd()
pretty_print(path, 0)
