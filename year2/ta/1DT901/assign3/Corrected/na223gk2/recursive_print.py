import os

directory_path = os.getcwd()
# directory_path = os.chdir("assignment_2")
# os.getcwd()


def print_dir(path):
    if os.path.isdir(path):
        for item in os.listdir(path):
            # item_path = os.path.join(path, item)
            if os.path.isfile(item):
                print(item, '\n')
            # print(f"File: {item_path}")
            elif os.path.isdir(item):
                print_dir(item)


executor = (print_dir(directory_path))
print(executor)
