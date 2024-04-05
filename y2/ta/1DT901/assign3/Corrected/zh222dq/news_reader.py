import os


# Function for getting words
def get_words(path, file_name):
    full_text = path + file_name
    words = "abcdefghijklmnopstqrvwxyz'- "
    not_words = "0123456789!@#$%^&*()=+{};:,.<>?/\|`~[]"
    valid_words = ""
    with open(full_text, "r", encoding="utf-8") as file:
        text = file.read()
        for t in text:
            if t.lower() in words:
                valid_words += t
            else:
                if t not in not_words:
                    valid_words += t
        valid_words = valid_words.split()
    return valid_words


# Function for saving words
def save_words(path, file_name, words):
    full_text = path + file_name
    with open(full_text, "w", encoding="utf-8") as file:
        for w in words:
            file.write(w + "\n")


# Main program
path = os.getcwd()
input_file = '\\data\\input\\swe_news.txt'

words = get_words(path, input_file)

output_file = '\\data\\output\\output_swe_news.txt'

save_words(path, output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)
