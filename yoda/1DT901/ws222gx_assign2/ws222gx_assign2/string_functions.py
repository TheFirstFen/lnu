def concat(s, n):
    new_string = ""
    for time in range(n):
        new_string += s
    return new_string


def count(s, x):
    counter = 0
    for char in s:
        if char == x:
            counter += 1

    return counter


def reverse(s):
    return s[::-1]


def first_last(s):
    if s != "":
        return s[0], s[-1]
    return "", ""


def has_two_X(s):
    x_counter = 0
    for char in s:
        if char == "X":
            x_counter += 1
            if x_counter == 2:
                return True
    return False


def has_duplicates(s):
    for index in range(len(s)-1):
        if s[index] == s[index + 1]:
            return True
    return False
