# Import random module
import random


# Function that returns sorted list without duplicates
def different(lst):
    a = set(lst)
    b = sorted(list(a))
    return b


# Start of program
lst = [random.randint(1, 200) for i in range(100)]

# Result
print("Different integers: ")
print(different(lst))
