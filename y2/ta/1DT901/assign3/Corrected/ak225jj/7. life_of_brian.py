import os


# reads the file
def read_file(path):
    with open(path, "r") as file:
        data = file.readlines()
    return data


# returns number of words
def get_words(path, input_file):
    clean_words = []
    data = read_file(path + input_file)
    allowed = ("abcdefghijklmnopqrstuvwxyzåäö-' ")
    for lines in data:
        lines = lines.lower()
        for i in lines:
            if i not in allowed:
                lines = lines.replace(i, "")
        lines = lines.split()
        for words in lines:
            clean_words.append(words)

    return clean_words


# prints every word on a single line
def save_words(path, output_file, words):
    with open(path + output_file, "w") as document:
        for word in words:
            document.write(word + "\n")


# Main program

path = os.getcwd()

input_file = '/data/life_of_brian.txt'

words = get_words(path, input_file)

output_file = f'/data/brian_{len(words)}_words.txt'

save_words(path, output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)
