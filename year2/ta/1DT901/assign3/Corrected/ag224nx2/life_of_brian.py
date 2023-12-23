import os


def get_words(row):
    row = row.lower()
    char_remove = ['!', '?', '.', ':', ',', '&', '"', '[', ']', '*']
    for char in char_remove:
        row = row.replace(char, '')

    lst_words_prow = row.split()

    lst_final_words = []
    for word in lst_words_prow:
        valid_word = True

        if len(word) > 1:
            i = 0
            while valid_word and i < len(word):
                if word[i].isdigit():
                    valid_word = False
                elif word[i] == 'å' or word[i] == 'ä' or word[i] == 'ö':
                    valid_word = False
                i += 1
        else:
            if word != 'a' or word != 'I':
                valid_word = False
        if valid_word:
            lst_final_words.append(word)
    return lst_final_words


def read_file(file_path):
    string_list_rows = []
    with open(file_path, 'r') as file:
        for row in file:
            string_list_rows.append(row)
    return string_list_rows


def save_words(file_path, words):
    with open(file_path, 'w') as file:
        for word in words:
            file.write(word + '\n')


def get_words_from_file(path):
    str_lst_rows = read_file(path)
    total_word_lst = []
    for row in str_lst_rows:
        if len(row.strip()) > 0:
            words_in_row_lst = get_words(row)
            total_word_lst.extend(words_in_row_lst)
    return total_word_lst


# program starts
path = os.getcwd() + '/texter/life_of_brian.txt'

words = get_words_from_file(path)
print(len(words))

output_file = f'texter/brian_{len(words)}_words.txt'

save_words(output_file, words)
