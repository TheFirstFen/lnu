import os


# Funktion som hittar alla mappar och sedan kör samma funktion i varje mapp
# för att få ut alla möjliga mappar
def print_sub(dir_path):
    lst1 = os.scandir(dir_path)
    for c in lst1:
        if (c.is_dir()):
            print(c.name)
            print_sub(c)


# Main program
os.chdir('..')
path = os.getcwd()
print_sub(path)

print(path)
