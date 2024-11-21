import random

sum = 0
print("Five random numbers:", end=" ")

# generates and prints out the random numbers
for n in range(5):
    number = random.randint(1, 100)
    sum += random.randint(1, 100)
    print(number, end=" ")

print("\nThe sum is", sum)
