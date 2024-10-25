import os


def count_py_lines(dir_path):
    directory = os.walk(dir_path)
    count_lines = 0

    for path, dirs, files in directory:
        for name in files:
            if name.endswith(".py"):
                search_path = os.path.join(path, name)
                lst = count_next(search_path)
                count_lines += len(lst)
    print(count_lines)


def count_next(dir_path):
    with open(dir_path, "r") as file:
        data = file.readlines()

        clean_data = []
        for ch in data:
            if ch.split():
                clean_data.append(ch.split())

    return clean_data


count_py_lines(os.getcwd())
