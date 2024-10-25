import os


# Creating a def called get_words with an empty list.
# open a file and for every line in the file we both strip and
# make every letter lowercase. for every letter in the line
# we replace does we dont want with a space and then add to the list.
def get_words(path, input_file):
    word_lst = []
    with open(path + "/" + input_file, "r", encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            line = line.lower()
            for letter in line:
                if 33 <= ord(letter) < 97 or ord(letter) == 171:
                    line = line.replace(letter, " ")
                if letter == "”":
                    line = line.replace("”", " ")
                if letter == "•":
                    line = line.replace("•", " ")
                if letter == "–":
                    line.replace("–", " ")
                if letter == "½":
                    line.replace("½", " ")
                if letter == "▪":
                    line.replace("▪", " ")
            if line != "":
                word_lst += line.split()
    return word_lst


# Creating a def called file_writer which for every word in words adds
# the word to a new file and then creats a new row for the next word.
def file_writer(output_file, words):
    with open(output_file, "w", encoding='utf-8') as file:
        for word in words:
            file.write(word)
            file.write("\n")


# Gets path
path = os.getcwd()
# Input file
input_file = '/data/swe_news.txt'

# variable which holeds the list from the function get_words.
words = get_words(path, input_file)
# Prints he amount of words in the list
print("Amount of words saved: ", len(words))
# output file/ where the words later is stored.
output_file = path + f'/data/swe_news_{len(words)}_words.txt'
# Calling the file_writer
file_writer(output_file, words)
