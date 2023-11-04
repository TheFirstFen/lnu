import os  # importera operating system

print()


# funktion för att räkna folders
def count_directories(dir_path):

    lst = os.scandir(dir_path)  # scana folder

    c_folder = 0

    for i in lst:  # Loop för alla folders i den valda folder
        if i.is_dir():
            c_folder += 1
    return c_folder


# funktion för att räkna files
def count_files(dir_path):

    lst = os.scandir(dir_path)  # scana folder

    c_folder = 0

    for i in lst:  # Loop för alla files i den valda folder
        if i.is_file():
            c_folder += 1
    return c_folder


# program start

path = r"C:\Users\yasin\Programming\1dv502\assignment-03"
# path till den nuvarande foldern som innehåler saker för att beräkna

# föra in pathen i funktionera för börja beräkna
print("The current directory:", path)
print("Folders:", count_directories(path))
print("Filse:", count_files(path))
