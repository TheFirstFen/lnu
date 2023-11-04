import os


# Returns a list of strings with the names of the directories
def list_dir(dir_path):
    lst = []
    entries = os.scandir(dir_path)
    for e in entries:
        if e.is_dir():
            lst.append(e.name)
    return lst


# Function for changing dir
def change_dir(changed_dir):
    os.chdir(changed_dir)


# Returns a list of strings with the names of the files
def list_files(dir_path):
    lst = []
    entries = os.scandir(dir_path)
    for e in entries:
        if e.is_file():
            lst.append(e.name)
    return lst


# Program starts
path = os.getcwd()

user_input = ""
while user_input != "4":
    print("1. List directories")
    print("2. Change directory")
    print("3. List files")
    print("4. Quit")
    print()
    user_input = input("==> ")
    if user_input == "1":
        lst = list_dir(path)
        for e in lst:
            print(e)
        print()
    elif user_input == "2":
        input_choise = input("Name of directory to enter: ")
        path = change_dir(input_choise)
        print()
    elif user_input == "3":
        lst = list_files(path)
        for e in lst:
            print(e)
        print()
    else:
        if user_input == "4":
            break
