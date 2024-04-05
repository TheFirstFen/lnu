# Import Os module
import os


# Function to get text from file
def get_string(path):
    with open(path, "r") as r:
        text = r.read()
    return text


# Function to count letter frequency
def count_letter(text, n):
    d = {}
    for letter in text:
        if letter != "-" and letter != "'" and letter != "\n":
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1
    sort_d = {k: v for k, v in sorted(d.items(), key=lambda tpl: tpl[0])}
    histogram = {k: "*"*int((v/n)) for k, v in sort_d.items()}
    return histogram


# Start of program
path = os.getcwd() + "\\assignment-03\\new_life_of_brian.txt"

text = get_string(path)

# The amount a star in the histogram represents
n = 500

dictionary = count_letter(text, n)

# Result
print("Reading text from file: ", path)
print(f"Total number of letters {len(text)}\n")
print("Histogram (where each star represents", n, "occurrences" +
      "of a given letter")

for k, v in dictionary.items():
    print(f"{k} | {v}")
