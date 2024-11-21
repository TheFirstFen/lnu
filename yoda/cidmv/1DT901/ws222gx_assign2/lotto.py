import random

lotto_numbers = []

while len(lotto_numbers) < 7:
    lotto_num = random.randint(1, 35)
    if not (lotto_num in lotto_numbers):
        lotto_numbers.append(lotto_num)

lotto_numbers = sorted(lotto_numbers)
print("The Lotto numbers this week:")
for num in lotto_numbers:
    print(num, end=" ")
