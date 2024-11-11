import os


# Help function that checks if string contains characters in alphabet
def check_if_word(str):
    for char in str:
        if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
            return True
        else:
            return False


# Help function that replaces symbols and returns the new string
def replace_symbols(str):
    temp_str = ""
    # Checks each character in string
    for char in str:
        if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
            l_char = char.lower()
            temp_str += l_char
            # Due to å, ä ,ö not being in ascii check these separate
        elif char == "å" or char == "Å" or char == "ä" or char == "Ä" \
                or char == "ö" or char == "Ö":
            l_char = char.lower()
            temp_str += l_char
        else:
            # If the symbol could be a part of a word replace with nothing
            if char == "'" or char == "-":
                temp_str += ""
            # If the symbol is between two words create a whitespace instead
            else:
                temp_str += " "
    return temp_str


# Returns a list of each word in provided file using help functions
def get_words(path, file_name):
    temp_lst = []
    b_lst = []
    # Opens and reads the file
    with open(path + file_name, "r") as file:
        as_string = file.read()
        n_string = as_string.strip()
        n_string = n_string.replace("\n", ", ")
        n_string = replace_symbols(n_string)
        lst = n_string.split(" ")
        for str in lst:
            if check_if_word(str) is True:
                temp_lst.append(str)
        for str in temp_lst:
            temp_str = replace_symbols(str)
            b_lst.append(temp_str)
        return b_lst


# Writes a new file with each elemnt in list on a new line
def save_words(path, output_file, words):
    with open(path + output_file, "w") as file:
        for word in words:
            file.write(word + "\n")


path = os.getcwd()
input_file = "/files2read/swe_news.txt"

words = get_words(path, input_file)


output_file = f"/data/swe_{len(words)}_words.txt"

save_words(path, output_file, words)
print('Saved', len(words), 'words in the file', path + output_file)
