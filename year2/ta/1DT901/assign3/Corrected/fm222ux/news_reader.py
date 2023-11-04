# Import os module
import os


# Function for reading file path into list
def read_file(file_path):
    lst = []
    with open(file_path, encoding='utf-8') as r:
        for line in r:
            lst.append(line.strip().lower())
    return lst


# Function for getting words
def get_words(lst):
    str = "abcdefghijklmnopqrstuvwxyzåäö -'"
    b = []
    new_lst = []
    for item in lst:
        for letter in item:
            if letter not in str:
                item = item.replace(letter, "")
                b = item.split()
        new_lst.extend(b)
    return new_lst


# Function to save words into new file
def save_words(lines, path):
    with open(path, "w", encoding='utf-8') as w:
        for i in lines:
            w.write(i)
            w.write("\n")


# Start of program
path = os.getcwd() + "\\assignment-03\\swe_news.txt"

save_path = os.getcwd() + "\\assignment-03\\new_swe_news.txt"

lst = read_file(path)

new_lst = get_words(lst)

save_words(new_lst, save_path)

print(f"Saved {len(new_lst)} words in file {save_path}")
