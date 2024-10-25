import os


def get_words(path, file_name):
    file_path = os.path.join(path, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    words = clean_words(text)
    return words


def clean_words(text):
    words = set()
    for line in text.split('\n'):
        line = line.strip()
        if line:
            words.update(line.split())
    return words


def save_words(path, file_name, words):
    file_path = os.path.join(path, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(words))


path = os.getcwd()
input_file = 'swe_news.txt'

words = get_words(path, input_file)

output_file = f'news_{len(words)}_words.txt'

save_words(path, output_file, words)
print('Saved', len(words), 'words in the file',
      os.path.join(path, output_file))
