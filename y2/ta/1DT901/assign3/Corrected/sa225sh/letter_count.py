import os


def read_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            file_content = file.read()
            return file_content


def counter(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha_dict = {
     'a': 0, 'b': 0, 'c': 0, 'd': 0,
     'e': 0, 'f': 0, 'g': 0, 'h': 0,
     'i': 0, 'j': 0, 'k': 0, 'l': 0,
     'm': 0, 'n': 0, 'o': 0, 'p': 0,
     'q': 0, 'r': 0, 's': 0, 't': 0,
     'u': 0, 'v': 0, 'w': 0, 'x': 0,
     'y': 0, 'z': 0
    }
    for s in string:
        if s in alphabet:
            alpha_dict[s] += 1
    return alpha_dict


def histogram(dict):
    tot_value = 0
    for key, value in dict.items():
        tot_value += value
    print(f"Total number of letters: {tot_value}")

    print("Histogram (where each star represents\
100 occurrences of the given letters)")
    for key, value in dict.items():
        stars_amount = value // 100
        stars = "*" * stars_amount
        print(f"{key} | {stars} \n")


# Tar han om path till filen och printar out resultaten,
# file[-17:-4] retuernar en seq som är filens nämn
file = "/Sa225sh_assign3/input/life_of_brian.txt"
path = os.getcwd() + file
print(f"Reading text from the file: {file[-17:-4]}")
string = read_file(path)
string = string.lower()
dict = counter(string)
histogram(dict)
