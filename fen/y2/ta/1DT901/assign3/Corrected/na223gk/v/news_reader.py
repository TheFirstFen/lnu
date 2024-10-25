import re
import time
import os


def extract_words(file_path):
    start_time = time.time()
    word_set = set()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())
            word_set.update(words)

    word_list = sorted(list(word_set))

    with open('swedish_words.txt', 'w', encoding='utf-8') as output_file:
        for word in word_list:
            output_file.write(word + '\n')

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Total execution time: {execution_time} seconds")


file_path = os.getcwd() + "/assignment_3/v/swe_news.txt"
extract_words(file_path)


# in this updated version, I've made the following changes:

# I added the re module to use regular expressions for word extraction.
# I used a set (word_set) to store unique words, which improves
# performance by eliminating duplicates.
# I used the findall method from the re module to extract all words
# from each line of the file.
# I converted the set word_set to a sorted list word_list before writing
# the words to the output file. This ensures that the words are written in
# alphabetical order.
# I added a timer to measure the execution time of the program.
