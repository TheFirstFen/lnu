import os


# Function to print all subderectories of current directory.
def print_sub(dir_path):
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir():
            print(entry.name)
            print_sub(entry)


"""
Main
"""

path = os.getcwd()

print_sub(path)
