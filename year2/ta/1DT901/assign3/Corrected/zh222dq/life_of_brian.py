import os


# Function for getting words
def get_words(path, file_name):
    full_text = path + file_name
    words = "abcdefghijklmnopstqrvwxyz'- "
    not_words = "0123456789!@#$%^&*()=+|[]{};:,.<>?/\`~"
    clear = ""
    with open(full_text, "r", encoding="utf-8") as file:
        file = file.read()
        for f in file:
            if f in words:
                clear += f
            else:
                if f not in words:
                    clear += f
        clear = clear.replace(not_words, "")
        clear = clear.split()
    return clear


# Function for saving words
def save_words(path, file_name, words):
    full_text = path + file_name
    with open(full_text, "w", encoding="utf-8") as file:
        for w in words:
            file.write(w + "\n")


# Main program
path = os.getcwd()
input_file = '\\data\\input\\life_of_brian.txt'

words = get_words(path, input_file)

output_file = '\\data\\output\\output_life_of_brian.txt'

save_words(path, output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)
