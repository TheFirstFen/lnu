import os

# Same as brian with different output


def read_file(file_path):  # Encoding with windows
    with open(file_path + "/data/swe_news.txt", "r", encoding="utf-8") as file:
        lst = file.readlines()
        return lst


def get_words(words):
    temp = []
    allowed_words = []
    words = read_file(file_path)
    symbols = ("'-abcdefghijklmnopqrstuvwxyzåäö")

    for c in range(len(words)):
        for char in words[c]:
            if char not in symbols:
                words[c] = words[c].replace(char, " ").lower()

        words[c] = words[c].strip("\n")
        temp.append(words[c].split(" "))

    for line in temp:
        for word in line:
            if len(word.replace(" ", "")) == 1:
                allowed_words.append(word)
            if word.isalpha() or word.isspace():
                allowed_words.append(word)
    return allowed_words


def save_words(file_path, words):
    with open(file_path + "/data/wordsinswe_news.txt",
              "w", encoding="utf-8") as output_file:
        for i in words:
            output_file.write(i + "\n")  # all words on new line in output


# Program starts
file_path = os.getcwd()

print(len(get_words(file_path)))
