import os


# Returns true if found file is hidden
def is_hidden(entry):
    return entry.name.startswith(".")


# Returns the number of directories found that is not hidden
def count_directories(dir_path):
    no_dir = 0
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir() and not is_hidden(entry):
            no_dir += 1
    return no_dir


# returns the amount of files found that is not hidden
def count_files(dir_path):
    no_fil = 0
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_file() and not is_hidden(entry):
            no_fil += 1
    return no_fil


path = os.getcwd()
print(f"I am right now at: {path}")
print(f"Below me i have {count_directories(path)} directories/folders")
print(f"This directory contains {count_files(path)} files")
