import random


def count_occurrences(lst):
    # return
    occurrences = {}

    # Counting the occurrences
    for num in lst:
        occurrences[num] = occurrences.get(num, 0) + 1

    return occurrences


if __name__ == "__main__":
    random_values = [random.randint(1, 10) for _ in range(100)]

    # occurrences dictionary
    result = count_occurrences(random_values)

    # printing the result
    for i in range(1, 11):
        print(f"{i}\t{result.get(i, 0)}")
