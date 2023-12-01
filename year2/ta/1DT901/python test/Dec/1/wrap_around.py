
def wrap(s, p):
    res = p
    for c in s:
        res += c + p
    return res


# ***************************
name = "Alice"
print(name, "==>", wrap(name, "--"))
