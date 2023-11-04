import os


def list_dir(dir_path):
    name_list = []
    entries = os.scandir(dir_path)
    for obj in entries:
        if obj.is_dir():
            name_list.append(obj.name)
    return name_list


def dir_change(new_dir):
    new_dir = os.chdir(new_dir)  # Chdir method to change current location
    return os.getcwd()


def list_files(file_path):
    name_list = []
    entries = os.scandir(file_path)
    for obj in entries:
        if obj.is_file():
            name_list.append(obj.name)
    return name_list


# Start program

path = "/Users/jape1"
run = True
while run:  # When the program is running the options will show
    print("\n1. List directories")
    print("2. Change directory")
    print("3. List files")
    print("4. Quit")
    inp = int(input("==> "))  # Input, write 1, 2, 3 or 4

    if inp == 1:
        lst = list_dir(path)
        for c in lst:
            print(c)

    elif inp == 2:
        ch_dir = input("Name of directory to enter: ")
        print("Changed to: ", dir_change(ch_dir))

    elif inp == 3:
        lst = list_files(path)
        for c in lst:
            print(c)

    elif inp == 4:
        break
