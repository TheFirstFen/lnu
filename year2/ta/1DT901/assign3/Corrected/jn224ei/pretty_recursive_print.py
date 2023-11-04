import os


# Funktion som hittar alla mappar och ändrar mellanrummet innan mappen i
# printen beroende på hur många mappar den har över sig
def pretty_print(dir_path, depth):
    lst = os.scandir(dir_path)
    for c in lst:
        if (c.is_dir()):
            print(("    "*depth)+c.name)
            pretty_print(c, depth+1)


pretty_print("./", 0)
