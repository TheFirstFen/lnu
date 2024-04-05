import string
import os


def count_letters(filename):
    letter_counts = {}
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                char = char.lower()
                if char in string.ascii_lowercase:
                    if char in letter_counts:
                        letter_counts[char] += 1
                    else:
                        letter_counts[char] = 1
    return letter_counts


def display_histogram(letter_counts):
    print("Letter Counts:")
    for letter, count in sorted(letter_counts.items()):
        print(f"{letter}: {'*' * count}")


def main():
    filename = os.getcwd() + "/assignment_3/v/life_of_brian.txt"
    letter_counts = count_letters(filename)
    display_histogram(letter_counts)


if __name__ == "__main__":
    main()
