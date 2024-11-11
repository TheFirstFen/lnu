import os


# Writes a new file with the content provided
def writing(path, name, content):
    with open(path + "/" + name, "w") as file:
        file.write(content)


new_s = ""
s = ""

f_name = input("Name of the file: ")
# Asks the user for a new input until "stop" is written
while new_s != "stop":
    s += new_s
    new_s = input("> ")
    # Creates a new line if input provided
    if s != "" and not new_s == "stop":
        s += "\n"


path = os.chdir("assignment-03/temp")
path = os.getcwd()
writing(path, f_name, s)
