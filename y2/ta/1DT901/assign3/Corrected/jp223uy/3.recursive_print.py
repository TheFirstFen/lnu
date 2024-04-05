import os


def print_sub(dir_path):  # Function in function
    entries = os.scandir(dir_path)
    for obj in entries:
        if obj.is_dir():
            print(obj.name)  # Print all subdirectories found
            print_sub(obj.path)  # Repeat the functions use until no more dir


# Program starts
path = os.getcwd()
print_sub(path)
