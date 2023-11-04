import os


def get_words(path, file_name):
    with open(path + file_name, "r", encoding="utf-8") as file:
        data = file.readlines()
    return cleaning(data)


def cleaning(new_data):

    # replaces \t with "" and also splits it to remove \n
    new_data = "".join(new_data).replace("\t", "").split()

    allowed_symboles = ("'-abcdefghijklmnopqrstuvwxyzåäö")
    # goes through each element in new_data list
    for value in range(len(new_data)):
        # goes through each charachter in new_data
        for char in new_data[value].lower():
            if char not in allowed_symboles:
                new_data[value] = new_data[value].replace(char, "")

    # creates a new list and returns the clean data
    return " ".join(new_data).split()


def save_words(path, file, words):
    with open(path+file, "w", encoding="utf-8") as f:
        for word in words:
            f.write(word+"\n")


path = os.getcwd()
input_file = '/data/swe_news.txt'

words = get_words(path, input_file)

output_file = f'/data/swe_news_{len(words)}_words.txt'

save_words(path, output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)
