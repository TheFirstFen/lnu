import os

# funktion för att lista kataloger i sökvägen
def list_dir(dir_path):
    directories = []
    for name in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, name)):
            directories.append(name)
    return directories

# funktion för att veta filer i sökvägen
def list_file(dir_path):
    files = []
    for name in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, name)):
            files.append(name)
    return files


current_dir = os.getcwd()

while True:
    print("\n1. List directories")
    print("2. Change directory")
    print("3. List files")
    print("4. Quit")
#den kör vall 1 som i sitt sätt vissa alla kataloger i file
    choice = input("\n==>")
    if choice == "1":
        directories = list_dir(current_dir)
        for directory in directories:
            print(directory)
# vall 2 att byta filen till en ny
    elif choice == "2":
        new_dir = input("Name of directory to enter: ")
        new_path = os.path.join(current_dir, new_dir)
        if os.path.isdir(new_path):
            current_dir = new_path
        else:
            print("Directory does not exist! ")
# lista för filer
    elif choice == "3":
        files = list_file(current_dir)
        for file in files:
            print(file)
# val 4 är att stänga programmet
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
