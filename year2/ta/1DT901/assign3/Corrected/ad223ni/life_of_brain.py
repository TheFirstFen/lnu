import os


def get_words(path, file_name):
    file_path = os.path.join(path, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        script = file.read()
    words = clean_words(script)
    return words


def clean_words(script):
    words = []
    current_word = ''
    for char in script:
        if char.isalpha() or char == "'" or char == "-":
            current_word += char
        elif current_word:
            words.append(current_word.lower())
            current_word = ''
    if current_word:
        words.append(current_word.lower())
    return words


def save_words(path, file_name, words):
    file_path = os.path.join(path, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(words))


path = os.getcwd()
input_file = 'life_of_brian.txt'

words = get_words(path, input_file)

output_file = f'brian_{len(words)}_words.txt'

save_words(path, output_file, words)
print('Saved', len(words), 'words in the file',
      os.path.join(path, output_file))
