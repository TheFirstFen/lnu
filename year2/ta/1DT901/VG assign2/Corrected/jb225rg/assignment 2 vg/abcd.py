
# checks through all the combinations of a - d.
# does not check a and d for 0
for a in range(1, 9):

    for b in range(0, 9):

        for c in range(0, 9):

            for d in range(1, 9):

                # if 4 times abcd == dcba it prints a,b,c,d
                if 4 * (1000 * a + 100 * b + 10 * c + d) == \
                        (a + 10 * b + 100 * c + 1000 * d):
                    print(a, b, c, d)
