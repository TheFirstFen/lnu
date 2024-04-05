def sum100(lst):
    for i in range(0, len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == 100:
                # print(lst[i], lst[j])
                return True
    return False


# ****************
lst = [33, 5, 67, 98, 51]
print(lst, "==>", sum100(lst))
lst = [-27, 14, 67, 51, 127]
print(lst, "==>", sum100(lst))
lst = [33, 5, 61, 94, 51]
print(lst, "==>", sum100(lst))
