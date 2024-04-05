import os


#  Returns a list of strings with the names of the directories
def list_dir(dir_path):
    lst = []
    for entry in os.scandir(dir_path):
        if entry.is_dir():
            lst.append(entry.name)
    return lst


#  Returns a list of strings with the names of the files
def list_files(dir_path):
    lst = []
    for entry in os.scandir(dir_path):
        if entry.is_file():
            lst.append(entry.name)
        elif entry.is_dir():
            lst += list_files(entry.path)
    return lst


def main():
    current_path = os.getcwd()
    while True:
        # label
        print("1. List directories")
        print("2. Change directory")
        print("3. List files")
        print("4. Quit")
        user_input = input("==>")
        # option 1
        if user_input == "1":
            dir_list = list_dir(current_path)
            # print list of directory
            for entry in dir_list:
                print(entry)
        # option 2
        elif user_input == "2":
            new_dir = input("Name of directory to enter: ")
            if new_dir == "..":
                # change dir
                os.chdir("..")
                # get new change curent path
                current_path = os.getcwd()
            else:
                os.chdir(new_dir)
                current_path = os.getcwd()
        # option 3
        elif user_input == "3":
            lst_files = list_files(current_path)
            # print the current list of file in the directory
            for entry in lst_files:
                print(entry)
        # option 4 quit
        elif user_input == "4":
            break


main()

