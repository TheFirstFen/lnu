import os


# return a list where each word is an element
def get_words(path, file_name):
    # full path to the file
    full_path = path + file_name
    words = []
    # Swedish alphabets
    swe_alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzÅåÄäÖö"

    with open(full_path, "r", encoding="utf-8") as file:
        for line in file:
            # Step 1: Convert to lowercase
            line = line.lower()
            # For storeing the current word
            current_word = ""
            for char in line:
                # If char is alphabet or "'-"
                # Remove ".","!","?",":", number etc
                if char in swe_alphabet or char in "'-":
                    # Add to the current words
                    current_word += char
                else:
                    # If the current word is a string and not emty
                    if current_word:
                        # Single char word case like a and i
                        # swedish words with one char 'i' 'ö'
                        if len(current_word) == 1 and current_word in "iö":
                            # Append the word
                            words.append(current_word)
                        else:
                            # Append the current word
                            words.append(current_word)
                    # Reset the current word
                    current_word = ""
            # When a line ends with a word case
            if current_word:
                words.append(current_word)
    return words


def save_words(path, file_name, words):
    # Full path
    full_path = path + file_name
    with open(full_path, "w", encoding="utf-8") as file:
        for word in words:
            # Write in the new full path file
            file.write(f"{word}\n")


def main():
    # Main program
    path = os.getcwd()
    input_file = '\\assignment-03\\swe_news.txt'

    words = get_words(path, input_file)

    output_file = f'\\assignment-03\\swe{len(words)}_words.txt'

    save_words(path, output_file, words)
    print('Saved', len(words), 'words in the file', path + output_file)


main()
