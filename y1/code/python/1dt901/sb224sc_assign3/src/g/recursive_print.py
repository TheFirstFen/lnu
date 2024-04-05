# recursive_print.py
#
# Author: Samuel Berg
# Date: 03-Oct-2022

import os

'''print_sub(dir_path):
Prints out every single directory below
current directory.
'''


def print_sub(dir_path):
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir():
            print(entry.name)
            print_sub(entry.path)


# Main code
path = os.getcwd()
print_sub(path)
