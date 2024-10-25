import os


def get_words(path, input_file):
    the_file = path + input_file
    seq = read_file(the_file)
    extra_tecken = "0123456789!@#$%^&*()_=+[]{};:,.<>?/\\|`~"
    clean = ""
    # dubble for loop för att gå i alla ord sen alla bokstaver
    for s in seq:
        if s not in extra_tecken:
            clean += s
    clean = clean.split()
    return clean


def save_words(path, output_file, lst):
    the_file = path + output_file
    if os.path.isfile(the_file):
        with open(the_file, "w") as file:
            for word in lst:
                file.write(word + '\n')


def read_file(input_file):
    if os.path.isfile(input_file):
        with open(input_file, "r") as file:
            file_contet = file.read()
            return file_contet


path = os.getcwd()
input_file = "\Sa225sh_assign3\input\life_of_brian.txt"
words = get_words(path, input_file)
output_file = "\Sa225sh_assign3\output\output_brian.txt"
save_words(path, output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)
