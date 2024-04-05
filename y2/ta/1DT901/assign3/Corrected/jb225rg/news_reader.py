import os


# read the dile and save lines in list
def read_file(file_path):
    lines = []
    with open(file_path, 'r') as infile:
        for row in infile:
            row = row.lower()  # to lower case
            lines.append(str(row.strip()))
    return lines


def get_words(lines):
    words = []
    # allower symbols
    allowed_v = ["'", "-", "å", "ä", "ö"]
    for s in lines:
        for v in s:
            # if not a-z
            if ord(v) < 96 or ord(v) > 123:
                if v not in allowed_v:
                    # if not allowed then replace
                    s = s.replace(v, " ")
        s = s.split()  # split into individual words
        for w in s:
            words.append(w)  # add to list
    return words


# save into new file
def save_words(outfile_path, words):
    with open(outfile_path, 'w') as outfile:
        for word in words:
            # write word then line break
            outfile.write(word + "\n")


# main program
path = os.getcwd()
input_file = path + "/assignment3/swe_news.txt"  # path text

# get lines then words
lines = read_file(input_file)
words = get_words(lines)

# path to new write file
output_file_path = path + f'/assignment3/swe_news_{len(words)}_words.txt'
save_words(output_file_path, words)
print('Saved', len(words), 'words in the file', output_file_path)
