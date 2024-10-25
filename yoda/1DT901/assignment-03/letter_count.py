import os


def get_words(path, file_name):
    with open(path + file_name, "r", encoding="utf-8") as file:
        return file.readlines()


def count_letters(words):
    # creates a dict with the letters a - z
    letters_dict = {chr(key): 0 for key in range(97, 123)}
    for key in letters_dict:
        count = 0
        for word in words:
            count += word.lower().count(key)
        letters_dict[key] = count
    return letters_dict


def print_histograms(data, occurrences_divider):
    for key in data:
        stars = "*" * (data[key] // occurrences_divider)
        print(f"{key} | {stars}")


path = os.getcwd()
input_file = './data/brian_13374_words.txt'

words = get_words(path, input_file)

occur_div = 100
count = count_letters(words)


print(f"Reading text from file: {input_file}")
print("Total number of letters: ...")
print(f"\nHistogram (where each star represents {occur_div} "
      "occurrences of the given letters)")
print_histograms(count, occur_div)
