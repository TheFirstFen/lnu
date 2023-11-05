import os


# Function
def get_words(file_name):
    allowed_characters = "abcdefghijklmnopqrstuvwxyzåäö'-"
    words = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            word = ""

            for char in line.lower():
                if char in allowed_characters:
                    word += char

                elif word:
                    words.append(word)
                    word = ""

    return words


# Function to save words to a new file, one word per line
def save_words(file_name, words):
    with open(file_name, "w", encoding="utf-8") as file:
        for word in words:
            file.write(word + "\n")


# Main program
input_file = os.getcwd() + "/data/swe_news.txt"

words = get_words(input_file)

output_file = os.getcwd() + "/data/swe_news_" + str(len(words)) + "_words.txt"

save_words(output_file, words)
print("Saved", len(words), "words in the file", output_file)
