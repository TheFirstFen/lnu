import os


# counts occurences by reading file and adding to dictionary
def count_occurances(path, name):
    dct = {}
    # opens and reads file
    with open(path + "/data/" + name, "r") as file:
        for line in file:
            word = line.strip()
            # adds to dictionary if word is longer than 4
            if len(word) > 4:
                if word not in dct:
                    dct[word] = 0
                dct[word] += 1
        # create a sortable list from dictionary
        items = list(dct.items())
        # returns sorted list
        return sorted(items, key=lambda tpl: tpl[1])[::-1]


# prints the top 10 words in dictionary in a clean way
def print_top10(dct):
    for i in range(10):
        length = int(len(dct[i][0]))
        n = 15 - length
        dist = 0
        if i < 9:
            dist = 1
        print(f"{i + 1}.{dist * ' '} {dct[i][0]}{n * ' '}{dct[i][1]}")


# main part that calls each function for correct value
path = os.getcwd()
dct1 = count_occurances(path, "brian_13391_words.txt")
print_top10(dct1)
print()
dct2 = count_occurances(path, "swe_14553534_words.txt")
print_top10(dct2)
