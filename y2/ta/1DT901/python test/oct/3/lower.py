def only_lower(lst):
    lower = []
    for c in lst:
        if c in "abcdefghijklmnopqrstuvwxyz":
            lower += [c]
    return lower


print(only_lower(list("Jonas Lundberg ABCDxyz")))
