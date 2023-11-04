def get_number(a, b, c, d):
    return a*1000 + b*100 + c*10 + d


max_value = 9
for a in range(1, max_value):
    for b in range(max_value):
        for c in range(max_value):
            for d in range(1, max_value):
                i = get_number(a, b, c, d)
                j = get_number(d, c, b, a)
                if 4 * i == j:
                    print(a, b, c, d)
