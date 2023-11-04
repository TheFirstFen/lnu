import os


# Lämnar tillbaka varje mapp i nuvarande mapp
def list_dir(dir_path):
    dir_list = []
    lst = os.scandir(dir_path)
    for c in lst:
        if c.is_dir():
            dir_list.append(c.name)
    return dir_list


# Byter mapp till det användaren väljer, samt printar ut alla val
def change_directory(dir_path):
    possible_directories = list_dir(dir_path)
    for c in possible_directories:
        print(c)
    print("Which directory would you like to change to? ('..') goes up one.")
    which_directory = input("==>")
    return which_directory


# Lämnar tillbaka varje fil i nuvarande mapp
def list_files(dir_path):
    file_list = []
    lst = os.scandir(dir_path)
    for c in lst:
        if c.is_file():
            file_list.append(c.name)
    return file_list


# Main program
running = True

# Användaren väljer funktion, den körs, därefter får användaren samma val.
# Detta pågår tills användaren väljer att stänga av programmet
while (running):
    path = os.getcwd()
    print("1. List directories")
    print("2. Change directory")
    print("3. List files")
    print("4. Quit")
    print()
    choice = int(input("==>"))
    if (choice == 1):
        dir_list = list_dir(path)
        for c in dir_list:
            print(c)
    elif choice == 2:
        new_directory = change_directory(path)
        os.chdir(new_directory)
    elif choice == 3:
        file_list = list_files(path)
        for c in file_list:
            print(c)
    elif choice == 4:
        break
    print()
