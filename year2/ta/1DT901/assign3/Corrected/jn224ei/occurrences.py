import random


# Funktion som räknar varje nummer och lägger in det som "key", därefter läggs
# varje nytt av det numret in som dess "value"
def count_occurrences(lst):
    numbers_dict = {}
    for i in range(1, 11):
        numbers_dict[i] = 0
    for num in lst:
        numbers_dict[num] += 1
    return numbers_dict


# Main program
# 100 random nummer mellan 1 och 10
random_list = []
for i in range(100):
    random_list.append(random.randint(1, 10))
numbers_dict = count_occurrences(random_list)

for k, v in numbers_dict.items():
    print(f"{k}\t{v}")
