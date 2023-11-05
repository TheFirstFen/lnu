import os


def is_valid_word(word):
    valid_characters = set("abcdefghijklmnopqrstuvwxyzåäö'-")
    return all(char in valid_characters for char in word)


def get_words(path, file_name):
    with open(os.path.join(path, file_name), 'r') as file:
        lines = file.readlines()
        words = []
        for line in lines:
            words.extend(word.strip(".,!?()[]{}\"").lower()
                         for word in line.split()
                         if is_valid_word(word.strip(".,!?()[]{}\"").lower()))
    return words


def save_words(path, file_name, words):
    with open(os.path.join(path, file_name), 'w') as file:
        for word in words:
            file.write(word + '\n')


if __name__ == "__main__":
    path = '/Users/sofiasvensson/Documents/Programmering/assignment-03'

    input_file = 'swe_news.txt'

    words = get_words(path, input_file)

    output_file = f'swe_{len(words)}_news.txt'

    save_words(path, output_file, words)
    print('Saved', len(words),
          'words in the file', os.path.join(path, output_file))
