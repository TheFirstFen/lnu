import os


def list_dirs(dir_path):
    dirs = os.scandir(dir_path)
    return [path.name for path in dirs if path.is_dir()]


def change_dir(dir_path):
    new_dir_path = os.path.abspath(dir_path)
    os.chdir(new_dir_path)


def list_files(dir_path):
    dirs = os.scandir(dir_path)
    return [path.name for path in dirs if path.is_file()]


def show_options():
    print("""
    1. List directories
    2. Change directory
    3. List files
    4. Quit
        """)


options = {1: list_dirs, 2: change_dir, 3: list_files}

show_options()
user_input = int(input("=> "))

while user_input != 4:
    dir_path = os.getcwd()
    if user_input == 2:
        name_of_dir = input("Name of directory to enter: ")
        options[2](name_of_dir)
    else:
        lst = options[user_input](dir_path)
        for content in lst:
            print(content)
    show_options()
    user_input = (int(input("=> ")))
