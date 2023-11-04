import random


# returns a list of all the unique values
def diffrent(lst): return list(set(lst))


lst = [random.randint(1, 200) for num in range(100)]
unique_lst = diffrent(lst)

print("Diffrent integers:")
print(unique_lst)
