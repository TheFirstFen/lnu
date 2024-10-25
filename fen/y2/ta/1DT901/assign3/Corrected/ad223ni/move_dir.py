import os


def list_dir(dir_path):
    directories = []
    for entry in os.scandir(dir_path):
        if entry.is_dir():
            directories.append(entry.name)
    return directories


def list_files(dir_path):
    files = []
    for entry in os.scandir(dir_path):
        if entry.is_file():
            files.append(entry.name)
    return files


while True:
    print("1. List directories")
    print("2. Change directory")
    print("3. List files")
    print("4. Quit")

    choice = input("==> ")
    if choice == "1":
        directories = list_dir(os.getcwd())
        for directory in directories:
            print(directory)
    elif choice == "2":
        directory_name = input("Name of directory to enter: ")
        os.chdir(directory_name)
    elif choice == "3":
        files = list_files(os.getcwd())
        for file in files:
            print(file)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
