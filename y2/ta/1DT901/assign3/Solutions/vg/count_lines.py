import os


def read_and_count(file_path):
    lines = 0
    with open(file_path, "r") as file:
        for line in file:
            s = line.strip()
            if len(s) > 1:
                lines += 1
    return lines


def count_py_lines(dir_path):
    py_count, line_count = 0, 0
    entities = os.scandir(dir_path)
    for e in entities:
        if e.is_dir():
            p, c = count_py_lines(e.path)
            py_count += p
            line_count += c
        elif e.is_file() and e.name.endswith(".py"):
            py_count += 1
            line_count += read_and_count(e.path)
    return py_count, line_count


# Program starts
path = os.getcwd()    # .../1DV501
py_file_count, line_count = count_py_lines(path)

print("Py-file count:", py_file_count, "\nPy-line count:", line_count)
