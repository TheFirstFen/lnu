import os


# counts non.empty lines
def count_py_lines(dir_path):
    rows = 0  # counter rows
    with os.scandir(dir_path) as entries:
        for entry in entries:

            # calls function again nor every directory found
            if entry.is_dir():
                rows += count_py_lines(entry)

            elif entry.is_file():
                # opens checks if .py file
                if entry.name.endswith(".py"):
                    # opens file
                    with open(entry, "r") as infile:
                        # go through the rows
                        for row in infile:
                            # if the roe length is > 1 it is not empty
                            if len(row) > 1:
                                rows += 1
    return rows


# main program
path = os.getcwd()
print(count_py_lines(path))
