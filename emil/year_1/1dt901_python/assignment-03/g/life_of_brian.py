import os


# Creat a def called get_words. empty list inside.
# open the input file and for every line in the file we both strip and
# make the text into lowercase words. For each letter in the line,
# if the ord of that letter matches one of the numbers its replaced with "".
# if the line does not contain nothing we split that line into a list.
# return the list.
def get_words(path, input_file):
    word_lst = []
    with open(path + "/" + input_file, "r") as file:
        for line in file:
            line = line.strip()
            line = line.lower()
            for letter in line:
                if 33 <= ord(letter) < 97:
                    line = line.replace(letter, "")
            if line != "":
                word_lst += line.split()
    return word_lst


# Creat a def called file_write. The same as in file_writer.py but it adds
# every word one by one from get_words.
def file_writer(output_file, words):
    with open(output_file, "w") as file:
        for word in words:
            file.write(word)
            file.write("\n")


# Gets the path
path = os.getcwd()
# Where to get the input file
input_file = '/data/life_of_brian.txt'

# variable which holeds the value from the function get_words
words = get_words(path, input_file)
# Where to put the words
output_file = path + f'/data/brian_{len(words)}_words.txt'
# calling the def file_writer
file_writer(output_file, words)

# print a blank line
print("\n")
# printing how many words and where does are saved
print('Saved', len(words), 'words in the file', path + output_file)
