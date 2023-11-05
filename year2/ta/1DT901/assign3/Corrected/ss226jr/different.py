import random


def different(lst):
    # returning the sorted list
    return sorted(set(lst))


if __name__ == "__main__":
    # create 100 random values
    random_values = [random.randint(1, 200) for _ in range(100)]

    # print the sorted list
    print("\nDifferent integers:\n", different(random_values))
