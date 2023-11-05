import os


def pretty_print(dir_path, depth=0):
    indent = ' ' * depth * 2
    print(indent + os.path.basename(dir_path))
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            pretty_print(item_path, depth + 1)


pretty_print('.')
