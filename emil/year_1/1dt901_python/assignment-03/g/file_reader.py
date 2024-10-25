import os


# Created a def called reading.
# opening with path and then the name of the file in read mode.
# variable set to 0.
# For each line in the file print all lines and add one to the counter.
# Return the variable.
def reading(path, name):
    with open(path + "/" + name, "r") as file:
        amount_of_lines = 0
        for line in file:
            print(line.strip())
            amount_of_lines += 1
    return amount_of_lines


# Get the path
path = os.getcwd()
# Asking for a file to read.
name = str(input("name of file to read: "))

# Printing the amounts of lines in that file.
print("amout of lines: ", reading(path, name))
