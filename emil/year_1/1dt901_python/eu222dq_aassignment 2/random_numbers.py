import random
amount_of_num = int(input("Enter the amount of numbers to compare: "))

min = 101
max = 0
number = 0
if amount_of_num < 1:
    print("Number must be 1 or larger")
else:
    for i in range(0, amount_of_num):
        random_num = random.randint(1, 100)
        print((random_num), end=' ')
        number += random_num
        if min > random_num:
            min = random_num
        if max < random_num:
            max = random_num
    average = round(((float(number / amount_of_num))), 2)
    print(f"average, min and max are {average}, {min} and {max}")
