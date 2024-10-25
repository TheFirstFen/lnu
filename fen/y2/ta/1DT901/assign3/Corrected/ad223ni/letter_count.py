import os


def count_letters(path, file_name):
    file_path = os.path.join(path, file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    letter_counts = {}
    for char in text:
        if char.isalpha() and char.isascii():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    return letter_counts


def display_histogram(letter_counts):
    histogram_title = "Histogram (where each star represents XXX occurrences" \
                      "of the given letters):"
    print(histogram_title)
    for letter, count in sorted(letter_counts.items()):
        histogram = '*' * count
        print(f"{letter} | {histogram}")


path = os.getcwd()
input_file = 'life_of_brian.txt'

print("Reading text from the file:", os.path.join(path, input_file))

letter_counts = count_letters(path, input_file)

total_letters = sum(letter_counts.values())
print("Total number of letters:", total_letters)

display_histogram(letter_counts)
