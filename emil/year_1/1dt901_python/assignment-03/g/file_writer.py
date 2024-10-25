import os


# Creating a def called.
# opening a new file with path then a name for the file.
# Adding the content the user wants to the file and makes a new row.
def writing(path, name, content):
    with open(path + "/" + name, "a") as file:
        file.write(content)
        file.write("\n")


# Gets path
path = os.getcwd()
# Asks for a name on the new file.
name = input("Enter a name of the file here: ")
# Printing out instructions for the program.
print('Enter content and end with "stop"')

# While loop to have the content put in the file or
# for the program to stop.
while True:
    content = input("")
    if content == "stop":
        break
    else:
        writing(path, name, content)
