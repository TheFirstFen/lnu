import os


# funktion för att läsa filen mamma mia. txt
def read_file(file_p):
    with open(file_p, "r") as file:
        lines = file.readlines()
    lst = str()

    for line in lines:
        line = line.strip()
        if line:
            lst += f"{line}\n"
        else:
            lst += "\n"

    return lst


# funktion för att skriva en kopia av mamma mia filen i in output file
def write_file(file_p, path):
    with open(path, "w") as file:
        file.write(file_p)


# föra in mamma mia texten i läs funktionet
path = os.path.join(os.getcwd(), "mamma_mia.txt")
fil = read_file(path)

# föra in en kopia av mamma mia text i den output filen eller txt
output_path = os.path.join(os.getcwd(), "Mamma_mia_text.txt")
write_file(fil, output_path)
