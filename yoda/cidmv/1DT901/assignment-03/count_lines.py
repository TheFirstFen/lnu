import os


def check_lenght_of_file(file):
    with open(file, 'r', encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
        non_empty_lines = [line.strip() for line in lines if line.strip()]
    return len(non_empty_lines)


def count_py_lines(dir_path):
    count_lines = 0

    for root, _, files in os.walk(dir_path):
        for name in files:
            if name.endswith(".py"):
                file_name = os.path.join(root, name)
                count_lines += check_lenght_of_file(file_name)

    return count_lines


path = "./"
print(count_py_lines(path))
