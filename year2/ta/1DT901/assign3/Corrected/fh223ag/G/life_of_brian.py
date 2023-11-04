import os
path = os.getcwd() + "/life_of_brian.txt"  # Path to txt file
write_path = os.getcwd() + "/new_life_of_brian.txt"  # Write path


def read_file(file_path):  # function used to open the file
    with open(file_path, "r") as file:
        full_text = ""
        for line in file:
            full_text += line
        return full_text


def get_words(row):  # Function used to get a pure words list
    word_split = []  # List used for the final text
    ft = row.lower()
    ft = ft.replace(":", " ")  # Replacing punctuation marks
    ft = ft.replace(".", " ")
    ft = ft.replace(",", " ")
    ft = ft.replace("!", " ")
    ft = ft.replace("?", " ")
    ft = ft.replace("[", " ")
    ft = ft.replace("]", " ")
    ft = ft.replace("&", " ")
    ft = ft.replace('"', " ")
    ft = ft.replace("'", " ")
    ft = ft.replace(";", " ")
    word_split = ft.split()
    for i in word_split:   # Go through all words in the list
        if i[0].isnumeric():
            word_split.pop(word_split.index(i))
        if i[0].isalpha() and i == i[0] * len(i):  # Check each word
            word_split.pop(word_split.index(i))  # for things like (iii)
    return word_split  # Return the final list


def save_words(file_path, words):  # Save words to write_path
    final_words = get_words(read_file(path))
    with open(file_path, "w") as file:
        for i in final_words:
            file.writelines(i + "\n")


words = get_words(read_file(path))  # used to get length of the word list
save_words(write_path, get_words(read_file(path)))  # Initialize functions
print("Saved ", len(words), "words in the file", write_path)  # Print results
