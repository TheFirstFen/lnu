# Constract the number using the diggits from find_digits
def get_number(a, b, c, d):
    return a * 1000 + b * 100 + c * 10 + d


# 4 nestlade for loops for att testa alla möjliga tal
def find_digits():
    for a in range(1, 10):
        for b in range(10):
            for c in range(10):
                for d in range(1, 10):
                    abcd = get_number(a, b, c, d)
                    dcba = get_number(d, c, b, a)

                    if dcba == 4 * abcd:
                        print(f"The four digits are a= {a}, b = {b}, c = {c}, \
d = {d}.")
                        print(f"The abcd digit is {a}{b}{c}{d}")


find_digits()
