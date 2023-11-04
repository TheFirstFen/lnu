import os


# A function to make a list of words.
def get_words(path, file_name):
    list_words = []
    with open(path + file_name, "r") as file:
        for line in file:
            lowered_line = line.lower()
            cleaned_line = clean_it(lowered_line)
            words = cleaned_line.split()
            for word in words:
                list_words.append(word)
    return list_words


# Function to save a word per line in a file.
def save_words(path, output_file, words):
    with open(path + output_file, 'w') as file:
        for word in words:
            file.write(word + '\n')


# Function to clean the text, excluding non-whitelisted characters.
def clean_it(line):
    new_line = ("")
    whitelisted = "abcdefghijklmnopqrstuvwxyz'-"
    for char in line:
        if char in whitelisted:
            new_line += char
        else:
            new_line += " "
    return new_line


"""
Main
"""
path = os.getcwd()
input_file = '/data/life_of_brian.txt'

words = get_words(path, input_file)

output_file = (f'/out/brian_{len(words)}_words.txt')

save_words(path, output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)
