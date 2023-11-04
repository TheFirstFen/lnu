import os
path = os.getcwd() + "/swe_news.txt"  # Path to txt file
write_path = os.getcwd() + "/new_swe_news.txt"  # Write path


def read_file(file_path):  # function used to open the file
    with open(file_path, "r") as file:
        full_text = ""
        for line in file:
            full_text += line
    return full_text


# For loop took too long so i removed it and used replace instead
# Although uglier it works faster since last version took about 1 hour
def get_words(row):  # Function used to get a pure words list
    word_split = []  # List used for the final text
    ft = row.lower()
    ft = ft.replace(":", " ")  # Replacing punctuation marks
    ft = ft.replace(".", " ")
    ft = ft.replace(",", " ")
    ft = ft.replace("!", " ")
    ft = ft.replace("?", " ")
    ft = ft.replace("[", " ")
    ft = ft.replace("]", " ")
    ft = ft.replace("&", " ")
    ft = ft.replace('”', " ")  # Added
    ft = ft.replace('"', " ")
    ft = ft.replace("-", " ")  # Added
    ft = ft.replace("½", " ")  # Added
    ft = ft.replace("•", " ")  # Added
    ft = ft.replace("▪", " ")  # Added
    ft = ft.replace("–", " ")  # Added
    ft = ft.replace("/", " ")  # Added
    ft = ft.replace("1", " ")  # Added
    ft = ft.replace("2", " ")  # Added
    ft = ft.replace("3", " ")  # Added
    ft = ft.replace("4", " ")  # Added
    ft = ft.replace("5", " ")  # Added
    ft = ft.replace("6", " ")  # Added
    ft = ft.replace("7", " ")  # Added
    ft = ft.replace("8", " ")  # Added
    ft = ft.replace("9", " ")  # Added
    ft = ft.replace("0", " ")  # Added
    for x in ft:    # Added to remove remaining digits
        if x.isdigit():
            ft = ft.replace(x, " ")
    word_split = ft.split()
    return word_split  # Return the final list


def save_words(file_path, words):  # Save words to write_path
    final_words = get_words(read_file(path))
    with open(file_path, "w") as file:
        for i in final_words:
            file.writelines(i + "\n")


words = get_words(read_file(path))  # used to get length of the word list
save_words(write_path, get_words(read_file(path)))  # Initialize functions
print("Saved ", len(words), "words in the file", write_path)  # Print results
