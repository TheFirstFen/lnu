def xor(a, b):
    if a and not b:
        return True
    elif not a and b:
        return True
    else:
        return False


# Main program starts
b = [True, False]
for i in b:
    for j in b:
        print(i, j, "==>", xor(i, j))
