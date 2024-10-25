import os


# Function to get words from a text file
def get_words(path, file_name):
    allowed_characters = list("abcdefghijklmnopqrstuvwxyz'-")
    words = []
    with open(file_name, "r", encoding="utf-8") as file:
        word = ""
        for line in file:
            for char in line:
                if char.lower() in allowed_characters:
                    word += char.lower()
                else:
                    if word:
                        words.append(word)
                    word = ""
        if word:
            words.append(word)
    return words


# Function to save words to a new file, one word per line
def save_words(path, file_name, words):
    with open(os.path.join(path, file_name), "w", encoding="utf-8") as file:
        for word in words:
            file.write(word + "\n")


# Main program
path = os.getcwd()
input_file = "data/life_of_brian.txt"

words = get_words(path, input_file)

output_file = f"data/brian_{len(words)}_words.txt"

save_words(path, output_file, words)
print("Saved", len(words), "words in the file", output_file)
