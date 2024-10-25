import os


# Creating a def called count diirectories. A variable is set to zero.
# If a entry from the path is a directorie it adds that amount to the
# variable.
def count_directories(path):
    dirs = 0
    directories, _ = is_entries(os.scandir(path))
    dirs += len(directories)
    return dirs


# Creating a def called count files. A variable is set to zero.
# If a entry from the path is a file it adds that amount to the
# variable.
def count_files(path):
    fil = 0
    _, files = is_entries(os.scandir(path))
    fil += len(files)
    return fil


# Creating a def called is_entry with two empty lists.
# For an entry it checks if its eather a dir or file.
# Appends the dir or file to the right list, returning both lists.
def is_entries(lst):
    direct = []
    fil = []
    for entry in lst:
        if entry.is_dir():
            direct.append(entry)
        elif entry.is_file():
            fil.append(entry)
    return direct, fil


# Gets the path
path = os.getcwd()
# Printing path
print(path)
# Printing the amount of dirs and files.
print(f"dir: {count_directories(path)}")
print(f"file: {count_files(path)}")
