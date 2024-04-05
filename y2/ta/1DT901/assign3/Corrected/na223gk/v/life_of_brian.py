import os


def get_words(path, file_name):
    # Read the script file
    with open(path + file_name, 'r') as file:
        script = file.read()

    # Clean the script by removing punctuation and converting to lowercase
    script = script.replace('\n', ' ').replace('\r', '')
    script = script.translate(str.maketrans('', '', '.,?!:;()[]'))

    # Split the script into words
    words = script.lower().split()

    return words


def save_words(words, output_file):
    # Save the words to a new file
    with open(output_file, 'w') as file:
        for word in words:
            file.write(word + '\n')


def main():
    path = os.getcwd() + "/assignment_3/v/"
    file_name = 'life_of_brian.txt'
    output_file = 'words.txt'

    # Get the words from the script
    words = get_words(path, file_name)

    # Save the words to a new file
    save_words(words, output_file)

    # Print the number of words and the output file name
    print(f"Number of words: {len(words)}")
    print(f"Words saved to file: {output_file}")


if __name__ == '__main__':
    main()
