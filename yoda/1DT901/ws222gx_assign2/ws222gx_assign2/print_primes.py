import time

wanted_primes = int(input("How many primes? "))
start = time.time()
"""
sets the 2 first primes to be able to check if later for certain,
if a number is a prime
"""
prime_lst = [2, 3]
count = prime_lst[-1] + 1   # first number to be checked if it is a prime
index = 0   # index of the first prime in the prime list
length_of_lst = 2   # length of the list (faster than len(prime_lst))

while length_of_lst < wanted_primes:
    prime = True
    count_const = int((count)**0.5) + 1

    # divides each potenial prime number up to that numbers square root
    for dividers in range(2, count_const):
        if (count % dividers == 0):
            prime = False
            break

    if prime:
        # divides each confirmed prime number with the potenial prime number
        # due to the number might be diviseble with that number
        while index < length_of_lst and index < count_const:
            if (prime_lst[index] % count == 0):
                prime = False
                break
            index += 1
        # if no break than it adds the number to the prime list
        else:
            prime_lst.append(count)
            length_of_lst += 1

    count += 1

if wanted_primes >= 2:
    for index, num in enumerate(prime_lst):
        if (index+1) % 10 == 0:
            print(num)
        else:
            print(num, end=" ")
else:
    print(prime_lst[0:wanted_primes])

print(time.time() - start)
