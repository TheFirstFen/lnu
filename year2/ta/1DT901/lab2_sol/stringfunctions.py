
def concat(s, n):
    return n*s


def count(s, x):
    n = 0
    for c in s:
        if c == x:
            n += 1
    return n


def reverse(s):
    st = ""
    for i in range(len(s), 0, -1):
        st += s[i-1]
    return st


def first_last(s):
    first = s[0]
    length = s[len(s)-1]
    return first, length


def has_two_X(s):
    n = 0
    for c in s:
        if c == "X":
            n += 1
    return n == 2


def has_duplicates(s):
    for i in range(0, len(s)-1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return True
    return False
