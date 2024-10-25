import os


def read_file(path):
    with open(path,  "r", encoding="utf-8") as file:
        return file.read()


def write_file(content, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


path = os.getcwd() + "/data/mamma_mia.txt"

# Read text file
lst = read_file(path)
print(f"Read {len(lst)} lines from file {path}")

# Write text file
path = os.getcwd() + "/data/output.txt"
write_file(lst, path)
print("Text saved in file", path)
