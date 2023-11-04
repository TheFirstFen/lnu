import os


# Funktion som läser filen och lägger in allt från filen i en sträng
def read_file(file_path):
    with open(file_path, "r") as file:
        text = ""
        for line in file:
            text += line
    return text


# Funktion som printar orden från den föregående filen
def write_file(lines, file_path):
    with open(file_path, "w") as file:
        file.writelines(lines)


# Main program

path = os.getcwd() + "/data/mamma_mia.txt"

text = read_file(path)

path = os.getcwd() + "/test.txt"

write_file(text, path)
