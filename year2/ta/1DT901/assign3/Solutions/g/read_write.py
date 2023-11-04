import os


# Safe file reading using with-as
def read_file(path):
    lines = []
    with open(path, "r") as file:
        for line in file:
            # print( line.strip() )
            lines.append(line)  # Including line break
    return lines


# Safe file writing handling IOErrors
def write_file(lines, path):
    with open(path, "w") as file:
        for line in lines:
            # print( line.strip() )
            file.write(line)  # Including line break


# Program starts
path = os.getcwd() + "/jlnmsi_assign3/mamma_mia.txt"

# Read text file
lst = read_file(path)
print(f"Read {len(lst)} lines from file {path}")

# Write text file
path = os.getcwd() + "/jlnmsi_assign3/output.txt"
write_file(lst, path)
print("Text saved in file", path)
