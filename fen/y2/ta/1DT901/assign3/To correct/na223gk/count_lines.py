import os


def count_py_lines(dir_path):
    count = 0

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    count += len([line for line in lines if line.strip()])

    return count


dir_path = os.getcwd()
line_count = count_py_lines(dir_path)
print(f"Total number of non-empty lines in Python files: {line_count}")
