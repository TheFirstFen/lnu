import os


# Creating a def called list_dir, which returns a list of directories.
def list_dir(dir_path):
    entries = os.scandir(dir_path)
    lst_dir, _ = is_entry(entries)
    return lst_dir


# Creating a def called is_entry with two empty lists.
# For an entry it checks if its eather a dir or file.
# Appends the dir or file to the right list, returning both lists.
def is_entry(path):
    direct = []
    file = []
    for entry in path:
        if entry.is_dir():
            direct.append(entry.name)
        elif entry.is_file():
            file.append(entry.name)
    return direct, file


# Creating a def called list_files, which returns a list of files
def list_files(dir_path):
    entries = os.scandir(dir_path)
    _, lst_file = is_entry(entries)
    return lst_file


# While loop that takes an input and eather prints, enters, leaves or shows the
# directories/files or exits the loop.
while True:
    print("1. List directories")
    print("2. Change directory")
    print("3. List files")
    print("4. Quit")
    n = input("\n==> ")
    if n == "1":
        for item in list_dir(os.getcwd()):
            print(item)
    elif n == "2":
        place = input("Name of directory to enter: ")
        os.chdir(place)
    elif n == "3":
        for item in list_files(os.getcwd()):
            print(item)
    elif n == "4":
        exit()
