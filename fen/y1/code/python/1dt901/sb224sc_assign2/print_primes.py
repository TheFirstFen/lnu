# print_primes.py
#
# Author: Samuel Berg
# Date: 01-Sep-2022

# Computes whether or not the given number is prime
def check_if_prime(N) -> bool:
    for i in range(2, N):
        if (N % i == 0):
            return False
    return True


# Creation "variables"
primes = []
N = -1

# Reads input
amount_of_primes = int(input('How many primes? '))


while (len(primes) < amount_of_primes):
    if (check_if_prime(N) and N > 1):
        primes.append(N)
        N += 1
    else:
        N += 1

for i in range(len(primes)):
    if (i == 0 or (i % 10) != 0):
        print(primes[i], end=' ')
    else:
        print(f'\n{primes[i]}', end=' ')
