# simple_math.py
#
# Author: Samuel Berg
# Date: 05-Sep-2022

def inc(n):  # Increments n with one
    return n + 1


def inc_with(n, t):  # Increments n with the value of t
    return n + t


def dec(n):  # Decrements n with one
    return n - 1


def dec_with(n, t):  # Decrements n with the value of t
    return n - t


def greatest(n1, n2):  # Returns the largest of the values n1 and n2
    return max(n1, n2)


def is_even(n):  # Returns True if n is even, otherwise false
    return n % 2 == 0


def power(x, n):  # Returns x to the power of n
    return x ** n


def factorial(n):  # Returns the factorial of n
    if n == 1:
        return n
    elif n < 1:
        return ('Not applicable')
    else:
        return n*factorial(n-1)


print('41 plus 1:', inc(41))
print('30 plus 12:', inc_with(30, 12))

print('43 minus 1:', dec(43))
print('52 minus 10:', dec_with(52, 10))

print('Which is greater, 24 or 42?', greatest(24, 42))

print('Is 42 even?: ', is_even(42))

print('2 to the power of 16:', power(2, 16))

print('Factorial of 5:', factorial(5))
