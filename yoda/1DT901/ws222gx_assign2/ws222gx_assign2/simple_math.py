def inc(n):
    return n+1


def inc_with(n, t):
    return n+t


def greatest(n1, n2):
    return n1 if n1 > n2 else n2


def is_even(n):
    return n % 2 == 0


def power(x, n):
    return x ** n


def factorial(n):
    fac = 1
    for i in range(n, 1, -1):
        fac *= i
    return fac


def is_prime(n):
    dividers = (2, 3, 5, 7)
    for i in dividers:
        if n % i == 0:
            return False
    return True


print('41 plus 1:', inc(41))
print('30 plus 12:', inc_with(30, 12))

print('Which is greater, 24 or 42?', greatest(24, 42))

print('Is 42 even?: ', is_even(42))

print('2 to the power of 16:', power(2, 16))

print('Factorial of 5:', factorial(5))
print('Is 41 a prime?:', is_prime(121))
