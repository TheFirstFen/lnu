import os


# Checks what is inside of each folder and displays it->
# ->Also prints the name of files inside of each folder
def print_sub(dir_path):
    entries = os.scandir(os.getcwd())
    for e in entries:
        if e.is_dir():
            print("Dir:", e.name)
            os. chdir(e)
            print_sub(e)
        if e.is_file():
            print("     ", e.name)


print_sub('')
