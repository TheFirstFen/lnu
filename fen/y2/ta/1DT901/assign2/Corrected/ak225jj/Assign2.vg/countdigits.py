n = input("Enter a large positive integer: ")
print()

count0 = 0
count_even = 0
count_odd = 0

for i in n:
    number = int(i)
    if number == 0:
        count0 += 1
    elif number % 2 == 1:
        count_odd += 1
    else:
        count_even += 1

print(f"Zeros: {count0}\nOdd: {count_odd}\nEven {count_even}")
