import os


def pretty_print(path, depth=0):
    space = "  "
    if os.path.isdir(path):
        for item in os.listdir(path):
            # item_path = os.path.join(path, item)
            if os.path.isdir(item):
                print(f"{space * depth} File: {item}")
                pretty_print(item, depth + 1)

            elif os.path.isfile(item):
                print("  " * depth, item)
            # print(f"File: {item_path}")


directory = os.getcwd()
pretty_print(directory)
