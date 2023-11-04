import os  # importera opreting systim


# funktion för att skriva ut undermappar av en path
def print_sub(dir_path):
    lst = os.scandir(dir_path)
    for i in lst:
        if i.is_dir():
            print(i.name)
            print_sub(i.path)  # kör funktionen rekursivt för undermappar


# sökvägen eller path
path = r"C:\Users\yasin\Programming\1dv502\1dv502_assignments"
print_sub(path)  # start utskrivt av undermappar
