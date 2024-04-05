import os


def pretty_print(dir_path, depth):

    dirs = os.scandir(dir_path)

    for entry in dirs:
        if entry.is_dir():
            # prints and mutliplies the white space with depth
            print("  "*depth, entry.name)
            new_path = os.path.join(dir_path, entry.name)
            # calls the pretty_print again but with new path and depth + 1
            pretty_print(new_path, depth+1)


pretty_print("./", 0)
