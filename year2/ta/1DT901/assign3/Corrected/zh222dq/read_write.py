import os


# Function that reades the file
def read_file(file_path):
    lst = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            lst.append(str(line))
    return lst


# Function that writes in the file
def write_file(lines, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        return file.writelines(lines)


# Program starts
path = os.getcwd() + "\\data\\input\\mamma_mia.txt"
print(path)

# Read text file
lst = read_file(path)
print(f"Read {len(lst)} lines from file {path}")

# Write text file
path = os.getcwd() + "\\data\\output\\output_mamma_mia.txt"
write_file(lst, path)
print("Text saved in file", path)
