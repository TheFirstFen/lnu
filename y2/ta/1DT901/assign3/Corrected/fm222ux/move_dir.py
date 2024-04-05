# Import Os module
import os


# List directory
def list_dir(path):
    entries = os.scandir(path)
    lst = []
    for item in entries:
        if item.is_dir():
            lst.append(item.name)
    return lst


# Change directory
def change_dir(new_dir):
    os.chdir(new_dir)


# List files
def list_file(path):
    entries = os.scandir(path)
    lst = []
    for item in entries:
        if item.is_file():
            lst.append(item.name)
    return lst


# Get current path
path = os.getcwd()

# Makes sure loop continues
Start = True

# Selection and implementation of options
while Start:
    # Print options
    print("1. List directories")
    print("2. Change directories")
    print("3. List files")
    print("4. Quit\n")
    choice = input("==> ")
    if choice == "1":
        # Get list and print items in list
        lst = list_dir(path)
        for item in lst:
            print(item)
        print()
    elif choice == "2":
        new_directory = input("Name of directory to enter: ")
        path = change_dir(new_directory)
        print()
    elif choice == "3":
        # Get list and print items in list
        lst = list_file(path)
        for item in lst:
            print(item)
        print()
        # Quit loop
    elif choice == "4":
        Start = False
