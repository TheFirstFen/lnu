import os


# A function to make a dictionary of occurances of letters in a text
def get_letters(path, file_name):
    # A dictionary from a to z with assigned value of 0.
    letter_list = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    with open(path + file_name, "r") as file:
        for line in file:
            lowered = line.lower()
            for char in lowered:
                if char in letter_list:
                    letter_list[char] += 1
    return letter_list


"""
Main
"""
path = os.getcwd()
input_file = '/data/life_of_brian.txt'

words = get_letters(path, input_file)

# Make the histogram, 1 star per 200 occurances in text.
print("Histogram")
for k, v in words.items():
    stars = (round(v / 200)) * "*"
    print(f"{k} | {stars}")
