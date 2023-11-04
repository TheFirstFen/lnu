import os

# funktion att rensa texteten från tecken


def clean(text):
    overs = set("!12#@3£¤4$%5&6/7{}()8[]=0+?´`^¨~*><|½§.,:\;äöå-'")
    cleaned = "". join([char for char in text if char not in overs])
    return cleaned.split()

# funktion att tar ord från en rad och retunerar efter man har rensat


def get_words_from_line(line):
    return clean(line)

# funktion som läser ord en fill och retuerar en lista av alla ord i filen


def get_words(path, input_file):
    file_path = os.path.join(path, input_file)
    all_words = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            all_words.extend(get_words_from_line(line))
    return all_words

# en funktion som sparar lista av or till en fil


def save_file(path, output_file, words):
    output_file_path = os.path.join(path, output_file)
    with open(output_file_path, "w",  encoding="utf-8") as file:
        for word in words:
            file.write(word + "\n")

# Här sprar man de man säger vart ska den sparas


path = os.getcwd()
input_file = "swe_news.txt"
output_file = "data/swe_news.txt"
words = get_words(path, input_file)
save_file(path, output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)
