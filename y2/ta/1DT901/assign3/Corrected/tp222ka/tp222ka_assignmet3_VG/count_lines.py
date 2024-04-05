import os


def count_py_lines(dir_path):
    # keeping tack of how many line
    count_lines = 0

    for entry in os.scandir(dir_path):
        # check if the file is a python file
        if entry.name.endswith(".py"):
            # counts non-empty lines in the file
            with open(entry.path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    # check if non-emty line
                    if line.strip() != "":
                        count_lines += 1
        elif entry.is_dir():
            # Recursive to sub -directories
            count_lines += count_py_lines(entry.path)
    return count_lines


def main():
    # path = os.getcwd()
    path = "C:\\lnu_uniwork\\python_courses\\1DT901"
    path = os.getcwd()
    total_line = count_py_lines(path)
    print(f"total python line you have write: {total_line}")


# run the program
main()
