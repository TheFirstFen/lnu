# abcd.py
#
# Author: Samuel Berg
# Date: 12-Sep-2022

''' get_number function:
Checks for all the generated numbers when "a,b,c,d" * 4 is equal to "d,c,b,a"
and prints what number of "a, b, c, d" that is
'''


def get_number(a, b, c, d):
    abcd = int(str(a) + str(b) + str(c) + str(d))
    dcba = int(str(d) + str(c) + str(b) + str(a))
    if (4 * abcd) == dcba:
        print(abcd)


# List with all the integers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generates all the different combinations of four integers
for a in numbers:
    if a != 0:
        for b in numbers:
            for c in numbers:
                for d in numbers:
                    if d != 0:
                        get_number(a, b, c, d)
