import os
path = os.getcwd()


def main_menu():
    print("\n")
    print("1. List directories")
    print("2. Change directory")
    print("3. List Files")
    print("4. Quit")
    return ''


def listdirs():
    dirs = os.listdir(os.getcwd())
    for items in dirs:
        if os.path.isdir(items):
            print(items)


def changedir():
    newdir = input("Name of directory to enter: ")
    if newdir == '...':
        current_dir = os.getcwd()
        dirlog = current_dir.split(os.path.sep)
        pastdir = os.path.sep.join(dirlog[:-1])
        os.chdir(pastdir)
    else:
        os.chdir(newdir)


def listfiles():
    files = os.listdir(os.getcwd())
    for items in files:
        if os.path.isfile(items):
            print(items)


def interacting():
    while True:
        main_menu()
        interact = input("==> ")
        if interact == '1':
            listdirs()
        elif interact == '2':
            changedir()
        elif interact == '3':
            listfiles()
        elif interact == '4':
            break


if __name__ == "__main__":
    interacting()
