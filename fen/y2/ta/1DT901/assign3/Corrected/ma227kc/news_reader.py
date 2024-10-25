import os


# Function needed
def get_words(path, file_name):
    wrds = []
    file_path = os.path.join(path, file_name)

    # automatically closing files after opening and being done with them
    # Code did not work in the beginning because of the Swedish characters
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.lower()
            for word in line.split():
                clean = ''.join(char for char in word
                                if char.isalpha() or char in ("-"))
                if clean == '-':
                    pass
                elif len(clean) != 0:
                    # expend() save each word in line as one element in words
                    # append() save all word in line as one element in words
                    wrds.extend([clean])

    return wrds


# The directory
path = "C:/Users/moham/source/pythonrepos/assignment-03/NEW"
name = "swe_news.txt"


# What was given in the exercise
words = get_words(path, name)
output_file = f'news_{len(words)}_words.txt'


# Function to save the file
def save_words(path, pathname, words):
    path = os.path.join(path, pathname)
    with open(path, 'w',  encoding='utf-8') as file:
        file.write("\n".join(words))


save_words(path, output_file, words)
# Displaying results
print('Saved', len(words), 'words in the file', path + output_file)
