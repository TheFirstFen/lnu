import os


# reads list and retirn lines as str in list
def read_file(file_path):
    lines = []
    with open(file_path, 'r') as infile:
        for row in infile:
            row = row.lower()  # make it lower case
            lines.append(str(row.strip()))
    return lines


# go through lines and return list of words
def get_words(lines):
    words = []
    allowed_v = ["'", "-"]  # allowed symbols
    for s in lines:
        for v in s:
            # checks if not a-z
            if ord(v) < 96 or ord(v) > 123:
                # checks if not allowed
                if v not in allowed_v:
                    # if not allowed then replaced
                    s = s.replace(v, " ")
        s = s.split()  # split into seperate words
        for w in s:
            words.append(w)  # add words to list
    return words


# writes words into a new text file
def save_words(outfile_path, words):
    with open(outfile_path, 'w') as outfile:
        for word in words:
            # write word and end with a line break
            outfile.write(word + "\n")


# main program
path = os.getcwd()
input_file = path + "/assignment3/life_of_brian.txt"  # path text

# get the lines then the words
lines = read_file(input_file)
words = get_words(lines)

# path to new file and function call
output_file_path = path + f'/assignment3/brian_{len(words)}_words.txt'
save_words(output_file_path, words)
print('Saved', len(words), 'words in the file', output_file_path)
