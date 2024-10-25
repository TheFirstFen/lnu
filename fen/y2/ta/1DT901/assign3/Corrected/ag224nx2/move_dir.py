import os


def list_dir(dir_path):
    listFold = []
    with os.scandir('.') as entries:
        for saker in entries:
            if os.path.isdir(saker):
                listFold.append(saker.name)
    return listFold
# for a in listFold:
#    print('\t' + a)


def change_dir():
    newDir = input('Enter directory you want to enter: ')
    subdir = os.chdir(newDir)
    return subdir


def lists_files(dir_path):
    lstFile = []
    en = os.scandir(dir_path)
    for e in en:
        if e.is_file():
            lstFile.append(e.name)
    return lstFile


user_input = ''
path = os.getcwd()

# program starts
while user_input != '4':
    print('1. List directories')
    print('2. Change directory')
    print('3. List files')
    print('4. Quit')
    print()
    user_input = input('==>')

    if user_input == '1':
        print('1. List directories')
        lstDir = list_dir(path)
        print(lstDir)

    elif user_input == '2':
        print('2. Change directory')
        here = os.getcwd()
        print('You are here: ', here)
        change_dir()
        print('Moved to directory: ', os.getcwd())
    # inpDir = input('Enter directory: ')
    # path = os.path.join(path, inpDir)

    elif user_input == '3':
        print('3. Lists files')
        path = os.getcwd()
        print(lists_files(path))

print('Goodbye!')
