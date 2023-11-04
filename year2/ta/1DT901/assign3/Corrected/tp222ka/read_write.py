import os


def read_file(file_path):
    lst = []
    # read file content
    with open(file_path, "r") as file:
        for line in file:
            # add it into the list
            lst.append(line)
    return lst


def write_file(lines, file_path):
    with open(file_path, "w") as file:
        # write the file from the give list
        file.writelines(lines)


def main():
    # Path to (mamma_mia.tt)
    path = os.getcwd() + "\\assignment-03\\mamma_mia.txt"

    # Read text file
    lst = read_file(path)
    print(f"Read {len(lst)} lines from {path}")

    # Write text file
    path = os.getcwd() + "\\assignment-03\\output.txt"
    write_file(lst, path)
    print("Text save in file", path)


# Run the program
main()
