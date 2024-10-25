# news_reader.py
#
# Author: Samuel Berg
# Date: 06-Oct-2022

import os
import zipfile

'''get_words(path, file_name):
Opens the specified file in the specified path
and converts each line into a index in a
list and then replaces all the specified characters
into spaces. Then it strips each line of new line
characters and then adds it all to a new list split
at each space character.
'''


def get_words(path, file_name):
    temp = []
    allowed_words = []
    with open(path + file_name, 'r', encoding='utf-8') as f:
        original = f.readlines()
        for line in original:
            line = line.lower()
            line = line.replace('-', '')
            line = line.replace("'", '')
            line = line.replace('.', ' ')
            line = line.replace(',', ' ')
            line = line.replace('!', ' ')
            line = line.replace('?', ' ')
            line = line.replace(":", ' ')
            line = line.strip('\n')
            temp.append(line.split(' '))

        for line in temp:
            for word in line:
                if len(word.replace(' ', '')) == 1:
                    if (word == 'a' or word == 'i'
                            or word == 'å' or word == 'ö'):
                        allowed_words.append(word)
                if word.isalpha() or word.isspace():
                    allowed_words.append(word)
        return allowed_words


'''save_words(path, name, words):
Creates a new file in specified path with given name
and computed words.
'''


def save_words(path, name, words):
    with open(path + name, 'a', encoding='utf-8') as f:
        for word in words:
            f.write(word + '\n')

# Main code
path = os.getcwd()
zip_file = '/data/swe_news.zip'
input_file = '/data/swe_news.txt'      # Changed

with zipfile.ZipFile(path + zip_file, 'r') as zip_ref:
    zip_ref.extractall(path + '/data/')


words = get_words(path, input_file)

output_file = f'/out/swe_news_{len(words)}_words.txt'      # Changed

save_words(path, output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)
