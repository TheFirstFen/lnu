import os


# funktion för files i den nuvarande folder
def list_files(dir_path):
    return [f for f in os.listdir(dir_path) if
            os.path.isfile(os.path.join(dir_path, f))]
# list comprehension för files i den den nuvarande path


# funktion för folders i den nuvarande folder
def list_directories(dir_path):
    return [d for d in os.listdir(dir_path)
            if
            os.path.isdir(os.path.join(dir_path, d))]
# list comprehension för folders i den den nuvarande path


# nuvarande folder eller pathen till den
current_dir = os.getcwd()

# wile loop för allternativerna
while True:
    print(f"\nCurrent Directory: {os.path.abspath(current_dir)}")
    print("\n1. List directories")
    print("2. Change directories")
    print("3. List files")
    print("4. Quit")
    choice = input("\n==> ")
    # om valet 1, lista alla folders
    if choice == "1":
        directories = list_directories(current_dir)
        for dir in directories:
            print(dir)
    # om valet 2, ändra pathen beror på inputen. Annars foldern finns inte
    elif choice == "2":
        new_dir = input("Name of directory to enter: ")
        new_path = os.path.join(current_dir, new_dir)

        if os.path.exists(new_path) and os.path.isdir(new_dir):
            os.chdir(new_path)
            current_dir = os.getcwd()
        else:
            print(f"Directory '{new_dir}' not found.")
    # om valet 3, lista alla files i nuvarande folder, eller den nya folder
    elif choice == "3":
        files = list_files(current_dir)
        for file in files:
            print(file)
    # valet 4 för att breaka loopen
    elif choice == "4":
        break
    # om inget av ovanstående, får användaren felmedelande
    else:
        print("Invalid choice. Please choose a valid option (1, 2, 3, or 4).")
