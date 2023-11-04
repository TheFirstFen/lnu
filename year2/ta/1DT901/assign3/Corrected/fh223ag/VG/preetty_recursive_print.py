import os

path = os.getcwd()
depth = 0


# Function to print sub directories
def pretty_print(dir_path, depth):
    entries = os.scandir(dir_path)  # Scan for objects in current directory
    for e in entries:  # Check all objects in the folder
        if e.is_dir():  # If it's a diretory print the name and move into subs
            print(" " * depth + e.name)
            pretty_print(e.path, depth + 1)


# Run the program
pretty_print(path, depth)
