import os


# Returns true if entry is hidden
def is_hidden(entry):
    return entry.name.startswith(".")


# Prints each sub directory in the path provided
def print_sub(dir_path):
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir() and not is_hidden(entry):
            print(entry.name)
            path = os.chdir(entry)
            print_sub(path)
    path = os.chdir("..")


path = os.getcwd()
print_sub(path)
