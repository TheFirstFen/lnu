# Funktion som läser in alla ord från en fil
def read_file(path):
    doc = open(path, "r", encoding="utf-8")
    text = doc.read().lower()
    word_list = text.split()
    return word_list


# Funktion som räknar varje bokstav orden om de är giltiga bokstäver
def count_letters(lst, letters):
    letter_dict = {}
    for c in letters:
        letter_dict[c] = 0
    for word in lst:
        for char in word:
            if char in allowed_letters:
                letter_dict[char] += 1
    return letter_dict


# Main program

input_file = 'data/life_of_brian.txt'
allowed_letters = "abcdefghijklmopqrstuvwxyz"
word_list = read_file(input_file)
letter_dict = count_letters(word_list, allowed_letters)

# Representerar varje 100 utan en bokstav som en stjärna i ett histogram
for dic_key in letter_dict.keys():
    letter_dict[dic_key] = (letter_dict[dic_key] // 100)
    letter_dict[dic_key] = letter_dict[dic_key] * "*"
print("Histogram (where each star represents 100 occurences of the"
      + "given letters)")
for k, v in letter_dict.items():
    print(f"{k} | {v}")
