import os


def read_file(file_path):
    with open(file_path, 'r') as infile:
        lines = infile.readlines()
    return lines


def write_file(lines, file_path):
    with open(file_path, 'w') as file:
        file.writelines(lines)


# Input file path
input_file_path = os.getcwd() + "/data/mamma_mia.txt"

# Read text file
lines = read_file(input_file_path)
print(f"Read {len(lines)} lines from file {input_file_path}")

# Output file path
output_file_path = os.getcwd() + "/data/output.txt"

# Write text file
write_file(lines, output_file_path)
print("Text saved in file", output_file_path)
