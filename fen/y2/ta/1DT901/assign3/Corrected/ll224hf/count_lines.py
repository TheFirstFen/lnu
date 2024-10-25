import os


def count_py_lines(dir_path):
    # We have no lines, yet
    lines = 0
    for root, dir, files in os.walk(path):
        for file in files:
            # Make sure the file is a python file
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as current_file:
                    for line in current_file:
                        # count the lines
                        if line.strip():
                            lines += 1
    return lines


"""
Main
"""
path = os.getcwd()

# Print results
print("Total non-empty lines in all .py files in directory and" +
      f" sub-directories: {count_py_lines(path)}")
