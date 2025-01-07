from QuadHash import QuadHash
from word_frequency import WordFrequency


def clean_word(word):
    word = word.lower()
    for i in word:
        if not i.isalpha():
            word = word.replace(i, '')
    return word


def read_and_analyse_text(filename):
    word_table = QuadHash(101)

    # Classic Lovecraftian terms to look for
    lovecraft_terms = {
        'cthulhu',  # The great old one himself
        'necronomicon',  # The forbidden book
        'nyarlathotep',  # The crawling chaos
        'yuggoth',  # The alien planet
        'kadath',  # The dream-quest destination
        'azathoth',  # The nuclear chaos
    }

    # Code to read and analyse the frequency of the words above
    # Use clean_word(word) to clean up each word
    try:
        with open(filename, "r") as file:
            for line in file.readlines():
                words = line.split()
                for word in words:
                    word = clean_word(word)
                    if word in lovecraft_terms:
                        if word_table.contains(WordFrequency(word)):
                            word_table.get(WordFrequency(word)).frequency += 1
                        else:
                            word_table.add(WordFrequency(word))
        return word_table

    except FileNotFoundError:
        print(f'Error: Could not find file {filename}')
        return None


def main():
    word_table = read_and_analyse_text('lovecraft.txt')

    if word_table:
        print('Here are the frequencies of classic Lovecraftian terms')
        print('-' * 54)

        for item in word_table:
            if item.frequency > 0:  # Only include words that appear in the text
                print(f'{item.word.capitalize()}: {item.frequency} occurrences')


main()
