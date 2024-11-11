import os


# returns true if entry is hidden
def is_hidden(entry):
    return entry.name.startswith(".")


# Prints each subdirectory in the path provided
def print_sub(dir_path, count):
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir() and not is_hidden(entry):
            # For each directory entered add new tabs
            tabs = count * "    "
            print(f"{tabs}{entry.name}")
            path = os.chdir(entry)
            print_sub(path, count + 1)
            path = os.chdir("..")


path = os.getcwd()
print_sub(path, 0)
