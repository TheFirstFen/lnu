import random

# En def som innehåller en lista som ska innehålla sorterad nummer


def diffrent(lst):
    numbers = set(lst)
    return sorted(numbers)

# genretar en slump massigt tal från 1, 200 det ska innehålla bara 100 nummer där efter printa de


random_numbers = [random.randint(1, 200) for x in range(100)]
sorted_number = diffrent(random_numbers)
print(sorted_number)
