import os


# creates a set by reading files
def create_set(path, name):
    # opens and reads file
    with open(path + "/data/" + name, "r") as file:
        st = set()
        # for each line in file strip and add to set
        for line in file:
            new_s = line.strip()
            st.add(new_s)
        # return length of set aka number of unique words
        return len(st)


# main part that calls the function and prints the result
path = os.getcwd()
name1 = "brian_13391_words.txt"
print(f"Unique words in {name1}: {create_set(path, name1)}")
name2 = "swe_14553534_words.txt"
print(f"Unique words in {name2}: {create_set(path, name2)}")
