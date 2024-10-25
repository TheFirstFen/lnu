# Funktion för att skapa ett resulterande heltalsvärde
# m.h.a serie multiplikation och additon
def get_number(a, b, c, d):
    p = 1000*a + 100*b + 10*c + d
    return p


# Start of program
# a 1-10
for a in range(1, 10):
    # b 0-10
    for b in range(10):
        # c 0-10
        for c in range(10):
            # d 1-10
            for d in range(1, 10):
                # The number DCBA is equal to 4 times the number ABCD
                if 4 * get_number(a, b, c, d) == get_number(d, c, b, a):
                    print(get_number(a, b, c, d))
