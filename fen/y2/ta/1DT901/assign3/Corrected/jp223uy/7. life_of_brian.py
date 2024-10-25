import os


def read_file(file_path):
    with open(file_path + "/data/life_of_brian.txt", "r") as file:
        lst = file.readlines()  # Read all lines in lst
        return lst


def get_words(words):
    temp = []  # Two lists with different intentions
    allowed_words = []
    words = read_file(file_path)
    symbols = ("'-abcdefghijklmnopqrstuvwxyzåäö")  # Looking for symbols

    for c in range(len(words)):
        for char in words[c]:
            if char not in symbols:  # Replace if not in symbol
                words[c] = words[c].replace(char, " ").lower()

        words[c] = words[c].strip("\n")
        temp.append(words[c].split(" "))

    for line in temp:  # Go through the new list made
        for word in line:
            if len(word.replace(" ", "")) == 1:
                allowed_words.append(word)
            if word.isalpha() or word.isspace():
                allowed_words.append(word)
    return allowed_words


def save_words(file_path, words):
    with open(file_path + "/data/wordsinbrian.txt",
              "w", encoding="utf-8") as output_file:  # Encoding windows
        for i in words:
            output_file.write(i + "\n")  # All words on new line in output


# Program starts
file_path = os.getcwd()
output_file = "/data/wordsinbrian.txt"
print("Saved", len(get_words(file_path)),
      "words in the file", output_file)
