import os


# Returns a list of strings with the names of the directories
def list_dir(dir_path):
    return [d for d in os.listdir(dir_path)
            if os.path.isdir(os.path.join(dir_path, d))]


# Returns a list of strings with the names of the files
def list_files(dir_path):
    return [f for f in os.listdir(dir_path)
            if os.path.isfile(os.path.join(dir_path, f))]


# Hantera while loopen, Input från user
def program():
    current_directory = os.getcwd()
    kill_switch = True
    while kill_switch:
        print("\n1. List directories")
        print("2. Change directory")
        print("3. List files")
        print("4. Quit")

        choice = input("==> ")

        if choice == '1':
            directories = list_dir(current_directory)
            for d in directories:
                print(d)

        elif choice == '2':
            new_directory = input("Name of directory to enter: ")
            if new_directory == '..':
                current_directory = os.path.dirname(current_directory)
            else:
                new_path = os.path.join(current_directory, new_directory)
                if os.path.isdir(new_path):
                    current_directory = new_path
                else:
                    print("Directory does not exist.")

        elif choice == '3':
            files = list_files(current_directory)
            for f in files:
                print(f)

        elif choice == '4':
            kill_switch = False

        else:
            print("Invalid choice. Please enter a valid option (1-4).")


program()
