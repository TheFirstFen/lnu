import os
scriptpath = (os.getcwd() + "/life_of_brian.txt")


def all_words(path):
    replacesymbs = ['[', ']', '!', '?', '.', '(', ')', ',', ':', ';']
    with open(path, "r") as file:
        readfile = file.read()
        for symbols in replacesymbs:
            readfile = readfile.replace(symbols, '')
        wordssplit = readfile.lower().split()
        wordslist = list(wordssplit)
    return wordslist


def file_with_words(path, file_name):
    allwords = all_words(path)
    with open(file_name, "w") as file:
        for words in allwords:
            file.write(words + ", ")
    file.close()


writefile = os.getcwd() + "/write_lob.txt"
print(len(all_words(scriptpath)))
file_with_words(scriptpath, writefile)
