import os


def print_sub(dir_path):
    for entry in os.scandir(dir_path):
        # checking if it's directory
        if entry.is_dir():
            # print entry name
            print(entry.name)
            # change directory
            os.chdir(entry.path)
            # recursively call,
            print_sub(entry.path)


def main():
    # get current path
    current_path = os.getcwd()
    print_sub(current_path)


# run the program
main()
