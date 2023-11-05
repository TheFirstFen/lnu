def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


def write_file(lines, file_path):
    with open(file_path, 'w') as file:
        file.writelines(lines)


# Program starts
path = ("/Users/alaa/Desktop/"
        "Inledande Prgrammering/"
        "assignment-03/output.txt")

# Read text file
lst = read_file(path)
print(f"Read {len(lst)} lines from file {path}")

# Write text file
output_path = (
    "/Users/alaa/Desktop/"
    "Inledande Prgrammering/"
    "assignment-03/output.txt"
)
write_file(lst, output_path)
print("Text saved in file", output_path)
