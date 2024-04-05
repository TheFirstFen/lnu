import os


def count_py_lines(dir_path):
    total_lines = 0
    for file_path in find_files(dir_path):
        lines = read_file(file_path)
        for line in lines:
            if line.strip() and not line.strip().startswith("#"):
                total_lines += 1
    return total_lines


def find_files(path):  # Hitta alla filer som slutar med .py
    file_lst = [os.path.join(path, d) for d in os.listdir(path)
                if os.path.isfile(os.path.join(path, d)) and d.endswith(".py")]
    return file_lst


def read_file(path):
    # read och splita infon i filen för att räkna dem i count funktionen
    if os.path.isfile(path):
        with open(path, "r") as file:
            file_content = file.read()
            lines = file_content.split("\n")
            return lines


path = os.getcwd()

print(count_py_lines(path))
