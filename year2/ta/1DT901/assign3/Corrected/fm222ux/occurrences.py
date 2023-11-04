# Import random module
import random


# Function for counting occurrences of number 1-10 in list
def occurrences(lst):
    d = {}
    for number in lst:
        if number not in d:
            d[number] = 1
        else:
            d[number] += 1
    x = sorted(d.items(), key=lambda tpl: tpl[0])
    sort_d = {k: v for k, v in x}
    return sort_d


# Start of program
lst = [random.randint(1, 10) for i in range(100)]

sorted_dict = occurrences(lst)

for k, v in sorted_dict.items():
    print(k, "\t", v)
