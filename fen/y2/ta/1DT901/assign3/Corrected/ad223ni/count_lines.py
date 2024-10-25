import os


def count_py_lines(dir_path):
    total_lines = 0

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as py_file:
                    lines = py_file.readlines()
                    non_empty_lines = [line.strip() for line in lines if
                                       line.strip()]
                    total_lines += len(non_empty_lines)

    return total_lines


# Testa funktionen
directory_path = os.getcwd()
lines_count = count_py_lines(directory_path)
print(f"Totalt antal icke-tomma rader i Python-filer: {lines_count}")
