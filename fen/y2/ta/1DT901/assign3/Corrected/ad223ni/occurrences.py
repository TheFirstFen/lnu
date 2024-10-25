import random
from collections import defaultdict


def count_occurrences(lst):
    occurrence_dict = defaultdict(int)

    for num in lst:
        occurrence_dict[num] += 1

    sorted_dict = dict(sorted(occurrence_dict.items()))
    return sorted_dict


# Generate a list of 100 random integers ranging from 1 to 10
random_integers = [random.randint(1, 10) for _ in range(100)]

# Count the occurrences of integers
occurrence_dict = count_occurrences(random_integers)

# Print the occurrences
print("Occurrences:")
for num, count in occurrence_dict.items():
    print(f"{num}\t{count}")
