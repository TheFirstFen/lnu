def pascal_rec(lst, n):
    # base cases
    if len(lst) - 1 == n:
        return lst

    if n == 0:
        return [1]

    current_line = []
    current_line.append(1)  # first element is always 1

    for i in range(len(lst)-1):
        curr_sum = lst[i] + lst[i + 1]
        current_line.append(curr_sum)

    current_line.append(1)  # last element is always 1
    return pascal_rec(current_line, n)


def pascal_line(n):
    start_lst = []
    return pascal_rec(start_lst, n)


print(pascal_line(0))
print(pascal_line(1))
print(pascal_line(2))
print(pascal_line(3))
print(pascal_line(4))
print(pascal_line(5))
