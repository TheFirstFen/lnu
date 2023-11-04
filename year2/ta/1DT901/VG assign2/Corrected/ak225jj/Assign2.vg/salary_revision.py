start = input("Provide salaries: ")

salary = start.split()
num = [int(n) for n in salary]

# median
num = sorted(num)
if len(num) % 2 == 1:
    med = num[len(num)//2]
else:
    med1 = num[len(num)//2]
    med2 = num[(len(num)//2)-1]
    med = (med1 + med2) / 2

# avrerege
avg = sum(num) / len(num)
round(avg)

# gap
gap = max(num) - min(num)

print(f"Median: {round(med)}\nAverege: {round(avg)}\nGap: {gap}")
