import random
n = int(input("Enter number of integers to be generated: "))

if n < 1:
    print("It must be a positive number!")
    exit()

sum, min, max = 0, 101, -1
print("\nGenerated values:", end=" ")
for i in range(n):
    p = random.randint(1, 100)
    print(p, end=" ")
    sum += p
    if p < min:
        min = p
    if p > max:
        max = p
print()
avr = round(sum/n, 2)
print(f"Average, min, and max are {avr}, {min}, and {max}")
