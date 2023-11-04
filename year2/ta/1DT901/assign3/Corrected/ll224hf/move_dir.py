import os


# Function to list folders in a directory.
def list_dir(dir_path):
    folder_list = []
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_dir():
            folder_list.append(entry.name)
    return folder_list


# Function to list files in a directory.
def list_files(dir_path):
    folder_list = []
    entries = os.scandir(dir_path)
    for entry in entries:
        if entry.is_file():
            folder_list.append(entry.name)
    return folder_list


# Function to change directory base of input.
def change_dir():
    whereto = input("Name of directory to enter: ")
    os.chdir(whereto)
    path = os.getcwd()
    return path


path = os.getcwd()
print("currently at: ", path)
choice = 0

# While to loop, exit on input = 4
while choice != 4:
    print("1. List directories\n" +
          "2. Change directory\n" +
          "3. List files\n" +
          "4. Quit\n")
    choice = (input("==> "))

    if choice == "1":
        dirlist = list_dir(path)
        for entry in dirlist:
            print(entry)
        print()
    elif choice == "2":
        path = change_dir()
        print()
    elif choice == "3":
        filelist = list_files(path)
        for entry in filelist:
            print(entry)
        print()
    elif choice == "4":
        exit()
