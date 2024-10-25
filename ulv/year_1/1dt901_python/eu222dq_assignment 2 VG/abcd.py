def get_num(a, b, c, d):
    a *= 1000
    b *= 100
    c *= 10
    # returning the numbers
    return a + b + c + d


# checing every number between 1 and 10 for a
for a in range(1, 10):
    # checing every number between 1 and 10 for b
    for b in range(0, 10):
        # checing every number between 1 and 10 for c
        for c in range(0, 10):
            # checing every number between 1 and 10 for d
            for d in range(1, 10):
                # checking if a number that matches the assignment exists
                if get_num(a, b, c, d) == get_num(d, c, b, a) / 4:
                    # printing the number that meets the condition
                    print(get_num(a, b, c, d), get_num(d, c, b, a))
