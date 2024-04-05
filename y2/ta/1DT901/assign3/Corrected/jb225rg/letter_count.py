import os


# reads the file and returns the lines
def read_file(file_path):
    lines = []
    with open(file_path, 'r') as infile:
        for row in infile:
            row = row.lower()  # make it loewer case
            lines.append(str(row.strip()))  # add line to list
    return lines


# gets the individual words
def get_words(lines):
    words = []
    # the allowed symbols outside of a-z
    allowed_v = ["'", "-", "å", "ä", "ö"]
    # checks lines
    for s in lines:
        # checks each letter in each string in list
        for v in s:
            # if letter is not allowed
            if ord(v) < 96 or ord(v) > 123:
                if v not in allowed_v:
                    # if not allowed, replace
                    s = s.replace(v, " ")
        s = s.split()  # split strings into individual lines
        # add words to list of words
        for w in s:
            words.append(w)

    return words


# counts letters in words returns a dictionary of letters
def letter_count(words):
    letter = {}
    # goes through the allowed letters and adds them to a dictionary
    for w in words:
        for v in w:
             # if letter not slready in list, add the letter and value 0
            if v not in letter:
                letter[v] = 0
            # inclrase the value of found letter
            letter[v] += 1
    return letter


# main program
# file path
path = os.getcwd()
input_file = path + "/assignment3/life_of_brian.txt"

# get lines, then words, then letters
lines = read_file(input_file)
words = get_words(lines)
letters = letter_count(words)

# sort the letters into alfabethical order for print
key_sorted = sorted(letters.items(), key=lambda tpl: tpl[0])
# total number of letters
total = 0
for value in letters:
    total = total + letters[value]  # add all values


# print
print("Reading from the file: .../life_of_brian.txt")
print("Total number of letters:", total)
print()
print("Histogram (where each star represents 100 occurrences of" +
      "the given letters)")
# print the letters
for k, v in key_sorted:
    star = v//100 * "*"  # each star is 100 occurances
    print(f'{k} | {star}')
