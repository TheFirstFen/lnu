import os


def read_file(input_file):
    lst = []
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            lst.append(line.lower().split(" "))
    return lst


def cleanword(word):
    newword = ""
    for i in word:
        if i in alphabet:
            newword = newword + i
    return newword


def get_words(lines):
    lst = []
    for line in lines:
        for word in line:
            lst.append(cleanword(word))
    return lst


def save_words(output_file, words):
    with open(output_file, "w", encoding="utf-8") as file:
        for word in words:
            file.write(word + "\n")
    return


path = os.getcwd()
alphabet = "abcdefghijklmonpqrstuvwxyz'-"
input_file = path + '/swe_news.txt'
lines = read_file(input_file)
words = get_words(lines)
output_file = path + "/fixed_swe_news.txt"

save_words(output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)
