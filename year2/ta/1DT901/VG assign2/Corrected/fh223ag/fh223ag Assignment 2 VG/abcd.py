# Function called get_number to "make" the 4 digit int
def get_number(a, b, c, d):
    print(a + 10 * b + 100 * c + 1000 * d)


# Create quadruple nested for loop to find the number
for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(1, 10):
                abcd = 4 * (1000 * a + 100 * b + 10 * c + d)
                dcba = 1000 * d + 100 * c + 10 * b + a
                if abcd == dcba:
                    get_number(a, b, c, d)
