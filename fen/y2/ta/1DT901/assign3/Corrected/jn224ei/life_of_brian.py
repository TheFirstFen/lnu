import os


# Funktion som hittar alla ord i en fil som sedan skickas till nästa funktion
def get_words(path, input_file):
    doc_words = ""
    doc = open(path + input_file, "r", encoding="utf-8")
    doc_words = doc.readlines()
    doc.close()
    return clean_words(doc_words)


# Funktion som tar bort alla otillåtna tecken och lägger in alla ord i en lista
def clean_words(words):
    word_list = []
    for lines in words:
        for c in lines:
            if (c.lower() not in letters):
                lines = lines.replace(c, " ")
        line_list = lines.split()
        for new_word in line_list:
            word_list.append(new_word)
    return word_list


# Funktion som skriver varje ord i listan i en annan fil
def save_words(path, output_file, words):
    doc_out = open(path + output_file, "w", encoding="utf-8")
    for word in words:
        doc_out.write(word + "\n")


# Main program

letters = "abcdefghijklmnopqrstuvwxyzåäö-' "
path = os.getcwd()
print("path: ", path)
input_file = '/data/life_of_brian.txt'

words = get_words(path, input_file)
output_file = f'/data/brian_{len(words)}_words.txt'

save_words(path, output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)
