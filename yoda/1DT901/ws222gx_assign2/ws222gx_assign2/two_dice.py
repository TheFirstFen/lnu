import random

spin_times = 10_000
# creates a list and sets all the values to 0
frequency_lst = 11*[0]
print(frequency_lst)
for i in range(spin_times):
    num1, num2 = random.randint(1, 6), random.randint(1, 6)
    index = (num1 + num2) - 2
    frequency_lst[index] += 1


print(f"Frequency table (sum,count) for rolling two dices {spin_times} times")
for dice_number in range(11):
    print(dice_number+2, "\t", frequency_lst[dice_number])
