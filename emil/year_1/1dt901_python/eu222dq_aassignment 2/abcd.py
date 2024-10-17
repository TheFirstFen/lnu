def get_number(a, b, c, d):
    a *= 1000
    b *= 100
    c *= 10
    return a + b + c + d


for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(1, 10):
                if get_number(a, b, c, d) * 4 == get_number(d, c, b, a):
                    print(get_number(a, b, c, d), get_number(d, c, b, a))
