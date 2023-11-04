import os


def read_file(path):
    lines = []
    with open(path, "r") as file:
        for line in file:
            # print( line.strip() )
            lines.append(line.strip())  # Excluding line break
    return lines


def replace_dots(text):
    s = ""
    for c in text:
        if c in '.!?,:—"”':   # Can be extended
            s += " "
        else:
            s += c
    return s


def is_alpha(s):  # Pythons isalpha accept some words that i don't like
    for c in s:
        if c not in "abcdefghijklmnopqrstuvwxyåäö-":
            return False
    return True


def is_word(word):
    if is_alpha(word) or word.count("'") == 1:
        if len(word) == 1:
            return word in "aiåö"
        else:
            return True
    else:
        return False


# Expected student approach without regular expressions
def get_words(text):
    text = replace_dots(text)  # Replace .,?,!, ... with whitespace
    text = text.lower()
    raw_words = text.split()
    words = []
    for w in raw_words:
        if is_word(w):
            words.append(w)
    return words


def save_words(path, save_words):
    output = "\n".join(words)
    with open(path, "w") as file:
        file.write(output)


# Main program starts

# Read text as a list of sentences
home = os.getcwd()
# path = home +"/data/eng_news_10-sentences.txt"
# path = home + "/data/life_of_brian.txt"
path = home + "/data/swe_news.txt"
lines = read_file(path)
print(f"\nRead {len(lines)} lines from file {path}")

# Collect words
words = []
for line in lines:
    w = get_words(line)
    words += w

# Save words in file
outfile = f"output_{len(words)}_words.txt"
outpath = home + "/data/" + outfile
save_words(outpath, words)
print(f"Saved {len(words)} words in file {outpath}")
