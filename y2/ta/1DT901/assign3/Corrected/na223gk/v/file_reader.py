import os


# Open the file in read mode


def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


# This function writes a list of lines to a file
def write_file(lines, file_path):
    with open(file_path, 'w+')as file:
        for line in lines:
            file.write("\n", line)
    print(f"Text saved in file '{file_path}'.")


if __name__ == "__main__":

    input_path = os.getcwd() + "/assignment_3/v/mamma_mia.txt"
    output_path = os.getcwd() + "/assignment_3/v/mamma_mia.txt"

    lst = read_file(input_path)
    if lst:
        print(f"Read {len(lst)} lines from file {input_path}")
        write_file(lst, output_path)
