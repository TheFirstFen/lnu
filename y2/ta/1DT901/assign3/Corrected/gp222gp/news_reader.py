import os
scriptpath = os.getcwd() + "/swe_news.txt"
# Changes made from Life of Brian is that this also removes numbers, as
# the texts seem to have a lot of numbers. Result was given in <10 seconds on
# an okay computer, and the result was 15969984


def all_words(path):
    replacesymbs = ['[', ']', '!', '?', '.', '(', ')', ',', ':', ';', '1', '2'
                    + '3', '4', '5', '6', '7', '8', '9', '0']
    with open(path, "r", encoding='utf-8') as file:
        readfile = file.read()
        for symbols in replacesymbs:
            readfile = readfile.replace(symbols, '')
        wordssplit = readfile.lower().split()
        wordslist = list(wordssplit)
    return wordslist


print(len(all_words(scriptpath)))
