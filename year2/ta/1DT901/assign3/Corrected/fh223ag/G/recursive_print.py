import os

path = os.getcwd()


# Function to print sub directories
def print_sub(dir_path):
    entries = os.scandir(dir_path)  # Scan for objects in current directory
    for e in entries:  # Check all objects in the folder
        if e.is_dir():  # If it's a diretory print the name and move into subs
            print(e.name)
            print_sub(e.path)


# Run the program
print_sub(path)
