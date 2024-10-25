# Import Os module
import os


# Function of reading
def read_file(file_path):
    lst = []
    with open(file_path, "r") as r:
        for line in r:
            lst.append(line.strip())
    return lst


# Function for writing
def write_file(lines, path):
    with open(new_path, "w") as w:
        for i in lines:
            w.write(i)
            w.write("\n")


# Start of program

# File location
file_path = os.getcwd() + "\\assignment-03\\mamma_mia.txt"

new_path = os.getcwd() + "\\assignment-03\\newmamma_mia.txt"

# Result
lst = read_file(file_path)

write_file(lst, new_path)
