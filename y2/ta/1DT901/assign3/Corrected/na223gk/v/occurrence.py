import random
from collections import defaultdict


def count_occurrences(lst):
    occurrences = defaultdict(int)
    for num in lst:
        occurrences[num] += 1
    sorted_occurrences = dict(sorted(occurrences.items()))
    return sorted_occurrences


def main():
    random_integers = [random.randint(1, 10) for _ in range(100)]
    occurrences_dict = count_occurrences(random_integers)
    print("Occurrences:")
    for num, count in occurrences_dict.items():
        print(f"{num}: {count}")


if __name__ == "__main__":
    main()
