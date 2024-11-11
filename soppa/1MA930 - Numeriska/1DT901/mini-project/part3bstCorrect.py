import BstMap as bst
import os


# removes all words shorter than 4 from list
def remove_u4(lst):
    # checks all indexes in list
    for i in range(len(lst) - 1, -1, -1):
        # if length of given key is shorter than 4, remove key and value
        if len(lst[i][0]) <= 4:
            lst.pop(i)
    return lst


# prints the top 10 words more readable
def print_t10(lst):
    for i in range(10):
        length = int(len(lst[i][0]))
        n = 15 - length
        dist = 0
        if i < 9:
            dist = 1
        print(f"{i + 1}.{dist * ' '} {lst[i][0]}{n * ' '}{lst[i][1]}")


path = os.getcwd()
# creates a new empty map
map = bst.BstMap()

# reads file and adds its line and how many occurences to map
with open(path + "/data/brian_13391_words.txt", "r") as file:
    for lines in file:
        num = 0
        line = lines.strip()
        # if word from file doesnt exist in tree create new node with value 1
        if map.get(line) is None:
            map.put(line, 1)
        # if word exist retriev its value and add 1, then return with new value
        else:
            num = map.get(line)
            map.put(line, num + 1)


# creates an empty list and creates a list from map
lst1 = []
lst1 = map.as_list()

# sorts the list by occurences from highest to lowest
lst1.sort(key=lambda x: x[1], reverse=True)
remove_u4(lst1)
# takes out the top 10 in list
y = slice(10)
sl_lst1 = lst1[y]
# print the results from life of brian map
print("Top 10 words in life of brian:")
print_t10(sl_lst1)
print(f"Number of tree nodes: {map.size()}")
print(f"Max depth: {map.max_depth()}")
print(f"Number of leaf nodes: {map.count_leafs()}")


# create a new empty map for swe_news
map2 = bst.BstMap()

# reads file and adds its line and how many occurences to map
with open(path + "/data/swe_14553534_words.txt", "r") as file:
    for lines in file:
        num = 0
        line = lines.strip()
        # if word from file doesnt exist in tree create new node with value 1
        if map2.get(line) is None:
            map2.put(line, 1)
        # if word exist retrieve its value and add 1, then return new value
        else:
            num = map2.get(line)
            map2.put(line, num + 1)

# creates an empty list and create a list from map
lst2 = []
lst2 = map2.as_list()

# sort the list by occurences from highest to lowest
lst2.sort(key=lambda x: x[1], reverse=True)
remove_u4(lst2)
# takes out the top 10 from list
y = slice(10)
sl_lst2 = lst2[y]
# print results from swe news map
print()
print("Top 10 words in swedish news:")
print_t10(sl_lst2)
print(f"Number of tree nodes: {map2.size()}")
print(f"Max depth: {map2.max_depth()}")
print(f"Number of leaf nodes: {map2.count_leafs()}")
