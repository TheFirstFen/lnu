def positive(lst):
    positive_lst = []
    for i in lst:
        if i >= 0:
            positive_lst.append(i)
    return positive_lst


# Demo Code
original_lst = [-99, 70, 15, -9, -34, -81, 1, -29, 48, 69]
print('Original list:')
print(original_lst)
print('The function returns the following list:')
print(positive(original_lst))
