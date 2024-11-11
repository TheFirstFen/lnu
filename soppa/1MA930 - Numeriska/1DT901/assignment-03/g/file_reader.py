import os


# Reads the file and returns the content and the number of lines
def reading(path, name):
    text = ""
    n = 0
    with open(path + "/" + name, "r") as file:
        for line in file:
            text += line
            n += 1
    return text, n


os.chdir("assignment-03/temp")
path = os.getcwd()

name = input("What is the name of file to read? ")
text, n = reading(path, name)
print(f"Lines in file: {n}")
print("Content of file:")
print(text)
