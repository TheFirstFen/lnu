
number_of_primes = int(input("How many primes? "))

prime_count = 0
n = 1
while prime_count < number_of_primes:
    n += 1

    # Check if n is prime
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False

    # Book keeping and print out
    if is_prime:
        print(n, end=" ")
        prime_count += 1
        if prime_count % 10 == 0:  # Line break every 10th prime
            print()
