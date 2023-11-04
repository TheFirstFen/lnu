import os

lst_dir = []
lst_files = []
path = os.getcwd()
user_quit = False


# Functions
def list_dir(dir_path):
    entries = os.scandir(dir_path)
    for i in entries:
        if i.is_dir():
            lst_dir.append(i.name)


def list_files(dir_path):
    entries = os.scandir(dir_path)
    for i in entries:
        if i.is_file():
            lst_files.append(i.name)


s_one = "1. List directories"
s_two = "2. Change directory"
s_three = "3. List files"
s_four = "4. Quit"

print(f"{s_one} \n{s_two} \n{s_three} \n{s_four}\n")
user_directions = int(input("==> "))
while user_directions != 4:
    if user_directions == 1:
        list_dir(path)  # Run function to find dirs
        for i in range(len(lst_dir)):  # Print all dirs
            print(lst_dir[i])
        print(f"\n{s_one} \n{s_two} \n{s_three} \n{s_four}\n")  # Show options
        lst_dir.clear()  # Clear the list
        user_directions = int(input("==> "))  # Ask the user again for input
    elif user_directions == 2:
        new_path = input("Name of directory to enter: ")
        path = os.chdir(f"{new_path}")
        print(f"\n{s_one} \n{s_two} \n{s_three} \n{s_four}\n")  # Show options
        user_directions = int(input("==> "))  # Ask the user again for input
    elif user_directions == 3:
        list_files(path)  # Run function to find files
        for i in range(len(lst_files)):  # Print all files
            print(lst_files[i])
        print(f"\n{s_one} \n{s_two} \n{s_three} \n{s_four}\n")  # Show options
        lst_files.clear()  # Clear list
        user_directions = int(input("==> "))  # Ask the user again for input
