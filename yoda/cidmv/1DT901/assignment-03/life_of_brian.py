import os


def get_words(path, file_name):
    with open(path + file_name, "r", encoding="utf-8") as file:
        data = file.readlines()
    return cleaning(data)


def cleaning(new_data):
    new_data = "".join(new_data).replace("\t", "").split()

    allowed_symboles = ("'-abcdefghijklmnopqrstuvwxyzåäö")
    for value in range(len(new_data)):
        for char in new_data[value].lower():
            if char not in allowed_symboles:
                new_data[value] = new_data[value].replace(char, "")

    return " ".join(new_data).split()


def save_words(path, file, words):
    with open(path+file, "w", encoding="utf-8") as f:
        for word in words:
            f.write(word+"\n")


path = os.getcwd()
input_file = '/data/life_of_brian.txt'

words = get_words(path, input_file)

output_file = f'/data/brian_{len(words)}_words.txt'

save_words(path, output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)
