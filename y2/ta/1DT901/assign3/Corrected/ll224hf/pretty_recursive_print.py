import os


# Function to list a "tree" of directories from starting directory
# that goes into sub-directories. Indented with " |" per depth,
# where the count signifies the amount of recursive runs the function
# has done. This makes it a lot more clear on what folder contains what.
def pretty_print(dir_path, depth):
    depth += 1
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir():
            print("  |" * depth, entry.name)
            pretty_print(entry, depth)


path = os.getcwd()

pretty_print(path, -1)
