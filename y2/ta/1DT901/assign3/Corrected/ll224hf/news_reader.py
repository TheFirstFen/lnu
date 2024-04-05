import os


# A function to make a list of words.
def get_words(path, file_name):
    list_words = []
    with open(path + file_name, "r", encoding="utf-8") as file:
        for line in file:
            lowered_line = line.lower()
            cleaned_line = clean_it(lowered_line)
            words = cleaned_line.split()
            for word in words:
                list_words.append(word)
    return list_words


# Function to save a word per line in a file.
def save_words(path, output_file, words):
    whitelisted = ("iåö")
    with open(path + output_file, 'w') as file:
        words_num = 0
        for word in words:
            if len(word) == "1" and word in whitelisted:
                file.write(word + '\n')
                words_num += 1
            elif len(word) > 1:
                file.write(word + '\n')
                words_num += 1
    return words_num


# Function to clean the text, excluding non-whitelisted characters.
def clean_it(line):
    new_line = ("")
    whitelisted = "abcdefghijklmnopqrstuvwxyzåäö '-"
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
input_file = '/data/swe_news.txt'

words = get_words(path, input_file)

output_file = ('/out/swe__words.txt')

word_count = save_words(path, output_file, words)

# Renaming cause can't figure out how to get it right in the first place
os.rename('out/swe__words.txt', f'out/swe_{word_count}_words.txt')

print('Saved', word_count, 'words in the file', path + output_file)
