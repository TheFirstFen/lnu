import os


def read_file(file_path):
    with open(file_path + "/data/life_of_brian.txt", "r") as file:
        lst = file.readlines()
        return lst


def get_words(words):
    temp = []
    allow_words = []
    words = read_file(file_path)
    symbols = ("'-abcdefghijklmnopqrstuwvyzåäö")

    for ch in range(len(words)):
        for c in words[ch].lower():
            if c.lower() not in symbols:
                words[ch] = words[ch].replace(c, " ").lower()

        words[ch] = words[ch].strip("\n")
        temp.append(words[ch].split(" "))

    for line in temp:
        for word in line:
            if len(word.replace(" ", "")) == 1:
                allow_words.append(word)
            if word.isalpha() or word.isspace():
                allow_words.append(word)
    return allow_words


def save_words(file_path, words):
    with open(file_path + "/data/brianwords.txt", "w",
              encoding="utf-8") as output_file:
        for i in words:
            output_file.write(i + "\n")


file_path = os.getcwd()
all_words = save_words(file_path, get_words(file_path))

print(len(get_words(file_path)))
