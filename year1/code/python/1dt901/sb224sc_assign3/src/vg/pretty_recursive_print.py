# pretty_recursive_print.py
#
# Author: Samuel Berg
# Date: 04-Oct-2022

import os

'''pretty_print(dir_path, depth=1):
Prints out every single directory below
current directory but every time it goes
deeper into a folder the depth increases
making it easier for the user to see
where every directory is located.
'''


def pretty_print(dir_path, depth=1):
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir():
            print(' ' * depth, entry.name)
            pretty_print(entry.path, depth + 2)


# Main code
path = os.getcwd()
pretty_print(path)
