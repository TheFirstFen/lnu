
def get_number(a, b, c, d):
    return 1000*a + 100*b + 10*c + d


# Program starts
for A in range(1, 10):
    for B in range(10):
        for C in range(10):
            for D in range(1, 10):
                abcd = get_number(A, B, C, D)
                dcba = get_number(D, C, B, A)
                if dcba == 4*abcd:
                    print("A, B, C, D = ", end="")
                    print(A, B, C, D, sep=", ")
