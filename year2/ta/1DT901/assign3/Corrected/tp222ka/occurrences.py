import random


# returns a sorted dictionary
def count_occurrences(lst):
    # Dictionary
    dict_count = {}

    for num in lst:
        # If num seen in dict add 1
        if num in dict_count:
            dict_count[num] += 1
        else:
            # Not in the dict add to the dict
            dict_count[num] = 1
    # Sort dictionary based on keys
    dict_sorted = sorted(dict_count.items(), key=lambda tpl: tpl[0])
    return dict_sorted


def main():
    lst = []
    # Add 100 random number between 1-10
    for i in range(100):
        lst.append(random.randint(1, 10))
    result = count_occurrences(lst)
    # print label
    for i in range(len(result)):
        print(result[i][0], "\t", result[i][1])


# run the program
main()

