# calculates the number
def get_number(a, b, c, d):
    return 1000 * a + 100 * b + 10 * c + d


upper_value = 9

for a in range(1, upper_value):
    for b in range(upper_value):
        for c in range(upper_value):
            for d in range(1, upper_value):

                right_side = 4 * get_number(a, b, c, d)
                left_side = get_number(d, c, b, a)

                if left_side == right_side:
                    print(f"A: {a}, B: {b}, C: {c}, D: {d}")
