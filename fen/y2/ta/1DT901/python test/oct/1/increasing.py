def is_increasing(lst):
    for i in range(len(lst)-1):
        if lst[i] >= lst[i+1]:
            return False
    return True


# Program starts
list = [1, 2, 3, 4, 5, 6, 7]
print(is_increasing(list))

list = [1, 2, 2, 2, 4, 6, 7]
print(is_increasing(list))
