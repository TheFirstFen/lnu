def rotate_left(lst):
    if len(lst) == 0:
        return lst
    else:
        s = lst[0]
        for i in range(0, len(lst)-1):
            lst[i] = lst[i+1]
        lst[-1] = s
    return lst


lst = [1]
print("old list: ", lst)
print("New list: ", rotate_left(lst))
