def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


m = int(input("How manny primes should be printed: "))
n = 0
lista = []

while True:
    if is_prime(n) and n > 1:
        lista.append(n)
        n += 1
    else:
        n += 1
    if len(lista) == m:
        break

j = m // 10
q = 0
w = 10
for y in range(0, j+1):
    print(*lista[q:w])
    q += 10
    w += 10
