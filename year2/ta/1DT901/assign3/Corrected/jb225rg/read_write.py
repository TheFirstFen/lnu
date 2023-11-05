import os


# read file and add lines to a string
def read_file(file_path):
    lines = []

    # open the file and read it while adding the lines to a list
    with open(file_path, 'r') as r_file:
        for row in r_file:
            lines.append(str(row.strip()))  # strip to rid of \n
    return lines


# write lines into a new txt file
def write_file(line, file_path):
    # open the new file and add the lines from the list
    with open(file_path, 'w') as outfile:
        for i in line:
            outfile.write(i + '\n')  # add back \n


# main program start
path = os.getcwd() + "/assignment3/mamma_mia.txt"

# Read text file
lst = read_file(path)
print(f"Read {len(lst)} lines from file {path}")

# Write text file
path = os.getcwd() + '/assignment3/output.txt'
write_file(lst, path)
print("Text saved in file", path)
