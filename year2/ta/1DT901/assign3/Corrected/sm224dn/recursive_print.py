import os


def print_sub(dir_path):
    dir_lst = [x for x in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, x))]
    for file in dir_lst:
        print(file)
        next = os.path.join(dir_path, file)
        print_sub(next)


path = os.getcwd()
print_sub(path)
