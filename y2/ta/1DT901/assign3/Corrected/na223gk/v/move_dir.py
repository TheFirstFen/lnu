import os

current_directory = os.getcwd()


def iterator(dir_path):
    list = {1: "List directories", 2: "Change directory",
            3: "List files", 4: "Quit"}
    print("Make a choice: ", end=print())
    for n in list:
        print(f"{n}.", list[n])
    choice = int(input("Choose a number from 1 - 4: "))
    # Choice of action

    def count_directories(dir_path):
        dir_counter = []
        for folder in os.listdir(dir_path):
            # Checks if the folder is a directory
            if os.path.isdir(folder):
                dir_counter.append(folder)
        return dir_counter

    def change_dir(dir_path):
        new_dir = input("Enter the path to your desired directory: ")
        os.chdir(f"{new_dir}")
        return f"Moved to dir: {os.getcwd()}"

    def count_files(dir_path):
        dir_counter = []
        for file in os.listdir(dir_path):
            # Checks if the item is a file
            if os.path.isfile(file):
                dir_counter.append(file)
        return dir_counter

    def exit():
        return quit()

    if choice == 1:
        print(count_directories(dir_path))
    elif choice == 2:
        print(change_dir(dir_path))
    elif choice == 3:
        print(count_files(dir_path))
    elif choice == 4:
        print(exit())


executer = (iterator(current_directory))
