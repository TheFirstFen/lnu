
def inc(n):
    return n + 1


def inc_with(n, t):
    return n + t


def dec(n):
    return n - 1


def dec_with(n, t):
    return n - t


def greatest(n1, n2):
    return max(n1, n2)


def is_even(n):
    if n % 2 == 0:
        return True
    return False


def power(x, n):
    return x**n


def faktorial(n):
    a = 1
    for i in range(2, n+1):
        a *= i
    return a
# program starts


a = 41
b = 30
c = 12
d = 43
e = 52
f = 10
g = 24
h = 42
i = 42
j = 2
k = 16
l1 = 5

print(f'{a} plus 1: ', inc(a))
print(f'{b} plus {c}: ', inc_with(b, c))
print(f"{d} minus 1: ", dec(d))
print(f"{e} minus {f}: ", dec_with(e, f))
print(f"Whitch is greatest, {g} or {h}?", greatest(g, h))
print(f"Is {i} even?", is_even(i))
print(f"{j} to the power of {k}: ", power(j, k))
print(f"Factorial of {l1}:", faktorial(l1))
