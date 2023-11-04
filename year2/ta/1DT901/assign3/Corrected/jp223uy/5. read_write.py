import os


def read_file(file_path):
    lst = []
    with open(file_path, "r") as file:
        lst = file.readlines()  # Read all lines in lst
        return lst


def write_file(lst, file_path):  # Encoding to make it work in windows
    with open(file_path, "w", encoding="utf-8") as output_file:
        output_file.writelines(lst)


# Program starts
path = os.getcwd() + "/data/mamma_mia.txt"
lst = read_file(path)  # Call the read function

# Read text file
print(f"\nRead {len(lst)} lines from file {path}")  # f string = working better

# Write text file
path = os.getcwd() + "/data/output.txt"  # Save in new file
write_file(lst, path)  # Write in the new file
print("Text saved in file", path)
print()  # Make it cleaner
