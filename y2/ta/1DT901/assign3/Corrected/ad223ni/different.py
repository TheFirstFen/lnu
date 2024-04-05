import random


def different(lst):
    unique_elements = sorted(list(set(lst)))
    return unique_elements


# Generate a list of 100 random values ranging from 1 to 200
random_values = [random.randint(1, 200) for _ in range(100)]

unique_values = different(random_values)

print("Different integers:")
print(unique_values)
