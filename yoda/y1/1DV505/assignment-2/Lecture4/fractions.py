class Fraction:

    def __init__(self, n1, n2):

        if not (isinstance(n1, int) and isinstance(n2, int)):
            raise TypeError("Number 1 and 2 has to be integers")

        if n2 == 0:
            raise ValueError("Denominator cannot be zero")

        if n2 < 0:
            self.n2 = abs(n2)
            self.n1 = n1*-1
        else:
            self.n1 = n1
            self.n2 = n2
        self.simplify()

    def __find_gcd(self):
        self.gcd = 1
        k = 2
        # has to be positive temporally
        n1, n2 = abs(self.n1), abs(self.n2)
        while k <= n2 and k <= n2:
            if n1 % k == 0 and n2 % k == 0:
                self.gcd = k
            k += 1

    def simplify(self):
        self.__find_gcd()
        self.n1 //= self.gcd
        self.n2 //= self.gcd

    def __add__(self, new):
        numerator = (self.n1 * new.n2) + (new.n1 * self.n2)
        denominator = self.n2 * new.n2
        return Fraction(numerator, denominator)

    def __sub__(self, new):
        numerator = (self.n1 * new.n2) - (new.n1 * self.n2)
        denominator = self.n2 * new.n2

        return Fraction(numerator, denominator)

    def __truediv__(self, new):
        numerator = self.n1 * new.n2
        denominator = self.n2 * new.n1
        return Fraction(numerator, denominator)

    def __mul__(self, new):
        numerator = self.n1 * new.n1
        denominator = self.n2 * new.n2
        return Fraction(numerator, denominator)

    def __str__(self):
        return f"{self.n1} / {self.n2}"


f1 = Fraction(3, 4)
f2 = Fraction(2, 5)
print(f"f1: {f1}")
print(f"f2: {f2}")
print("\nCalculations:")

print(f"f1 + f2 = {f1 + f2}")
print(f"f1 - f2 = {f1 - f2}")

print(f"f1 * f2 = {f1 * f2}")
print(f"f1 / f2 = {f1 / f2}")

print("With negativ numbers")
f1 = Fraction(-3, 4)
f2 = Fraction(2, 5)
print(f"f1: {f1}")
print(f"f2: {f2}")
print("\nCalculations:")

print(f"f1 + f2 = {f1 + f2}")
print(f"f1 - f2 = {f1 - f2}")

print(f"f1 * f2 = {f1 * f2}")
print(f"f1 / f2 = {f1 / f2}")

print("\nTest with floating numbers")
try:
    f1 = Fraction(3.2, 4)
    f2 = Fraction(5, 4)
except TypeError as e:
    print(e)
