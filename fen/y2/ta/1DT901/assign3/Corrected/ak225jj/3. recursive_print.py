import os


def print_sub(dir_path):
    lst = os.scandir(dir_path)  # skapar en lista med alla info i mappen
    for path in lst:            # kollar alla vägar i mapparna
        if path.is_dir():       # kollar ifall vägen är en mapp
            print(path.name)    # printar namnet på mappen
            next_path = os.path.join(dir_path, path.name)
            print_sub(next_path)


print_sub(os.getcwd())
