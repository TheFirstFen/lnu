import os


# Safe file reading handling IOErrors
def read_file(path):
    lines = []
    try:
        with open(path, "r") as file:
            for line in file:
                # print( line.strip() )
                lines.append(line)  # Including line break
    except IOError as e:
        print(type(e), "==>", e)
        print("No such file: ", path)
    return lines


def count_letters(lines):
    # Initialize dict
    dct = {}
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for c in alpha:
        dct[c] = 0

    # Count chars in alpha
    for line in lines:
        for c in line:
            c = c.lower()
            if c in alpha:
                dct[c] += 1
    return dct


def print_histogram(dct, factor):
    for k, v in dct.items():
        v = v//factor
        s = v*"*"
        print(k, s)


# Monty Python's Life of Brien
path = os.getcwd() + "/data/life_of_brian.txt"
lines = read_file(path)

dct = count_letters(lines)
factor = 100
print("\nHistogram for", path, "using * =", factor)
# print(dct)
print_histogram(dct, factor)

# 100K sentences
path = os.getcwd() + "/data/eng_news_100K-sentences.txt"
lines = read_file(path)

dct = count_letters(lines)
factor = 10000
print("\nHistogram for", path, "using * =", factor)
# print(dct)
print_histogram(dct, factor)
