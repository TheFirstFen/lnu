# make a function that calculates the ABCD & DCBA numbers
def get_number(a, b, c, d):
    number = a * 1000 + b * 100 + c * 10 + d
    return number


# DCBA = 4 * ABCD
# A & D != 0

# Like the hint here, I made 4 nested loops that itterate through the possible
# numbers. And always checks if the combination works. once it's found a
# combination that works it prints it out. In this case only one works.
for A in range(1, 10):
    for B in range(0, 10):
        for C in range(0, 10):
            for D in range(1, 10):
                # 2 Variables, both get sent to function then checked
                # if they meet the condition. Done for all numbers.
                ABCD = get_number(A, B, C, D)
                DCBA = get_number(D, C, B, A)
                if DCBA == (4 * ABCD):
                    # Print results
                    print("A number that meets the conditions is:" +
                          f" {ABCD}")
