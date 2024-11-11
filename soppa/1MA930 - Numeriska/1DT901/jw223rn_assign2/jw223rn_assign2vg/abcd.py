# Function that creates a number from four different integers
def get_number(a, b, c, d):
    a = a * 1000
    b = b * 100
    c = c * 10
    return a + b + c + d


# Creates variables
a = 0
b = 0
c = 0
d = 0

""" A nested for loop to check each number in abcd so that the equation works,
as a and d cant be 0 it only checks for 1-9 instead of 0-9"""
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            for d in range(1, 10):
                # Prints the number abcd if equation is true
                if (4 * get_number(a, b, c, d)) == get_number(d, c, b, a):
                    print(get_number(a, b, c, d))
