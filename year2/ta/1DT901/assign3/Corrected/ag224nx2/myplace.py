import os

spaFile = []
spaFold = []


def count_directories(entr, pa):
    entr = os.scandir(pa)
    for en in entr:
        if en.is_dir():
            spaFold.append(en.name)
    return spaFold


def count_files(en, p):
    en = os.scandir(p)
    for e in en:
        if e.is_file():
            spaFile.append(e.name)
    return spaFile


# program starts
path = os.getcwd()
entries = os.scandir(path)


file_es = count_files(entries, path)
dir_es = count_directories(entries, path)

print('We are here:', path)
print('Number of files under this path:', len(file_es))
print('Number of folders/directories under this path:', len(dir_es))
