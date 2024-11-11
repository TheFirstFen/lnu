import HashSet as hset
import os


# returns the file provided as a list
def return_as_list(path, name):
    lst = []
    with open(path + "/data/" + name, "r") as file:
        for line in file:
            n_l = line.strip()
            lst.append(n_l)
    return lst


# create a new hashset for life of brian
words = hset.HashSet()
words.init()

path = os.getcwd()
lst = return_as_list(path, "brian_13391_words.txt")
# add all words in list to hashset
for name in lst:
    words.add(name)
# prints results
print("Life of brian results")
print("Unique words:")
print(words.get_size())
print("zero bucket ratio:")
print(words.zero_bucket_ratio())
print("max bucket size:")
print(words.max_bucket_size())
print("bucket list size")
print(words.bucket_list_size())

# create a new empty hashset for swe news
words2 = hset.HashSet()
words2.init()

lst2 = return_as_list(path, "swe_14553534_words.txt")
# add all words from new lst to new hashet
for name in lst2:
    words2.add(name)
# prints out the results
print()
print("Swe news results")
print("Unique words:")
print(words2.get_size())
print("zero bucket ratio:")
print(words2.zero_bucket_ratio())
print("max bucket size:")
print(words2.max_bucket_size())
print("bucket list size")
print(words2.bucket_list_size())
