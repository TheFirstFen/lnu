import os

summa = 0


def count_lines(path, depth=0):
    global summa
    dirs = os.scandir(path)
    for curr_path in dirs:
        if curr_path.is_dir():
            next_path = os.path.join(path, curr_path.name)
            print(" " * depth + curr_path.name)
            count_lines(next_path, depth + 1)

        elif curr_path.is_file() and curr_path.name.endswith(".py"):
            file_path = os.path.join(path, curr_path.name)
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
                non_empty_lines = [line.strip()
                                   for line in lines if line.strip()]
                summa += len(non_empty_lines)

            print(" " * depth + curr_path.name)


count_lines(os.getcwd())
print("Total lines:", summa)
