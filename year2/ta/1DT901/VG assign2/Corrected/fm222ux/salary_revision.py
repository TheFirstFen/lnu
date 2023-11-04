# Read salary input, convert to integers and sort in list
text = input("Provide salaries: ")

salaries = text.split()

salaries.sort()

salaries_int = [int(n) for n in salaries]

# Calculations for median, average and gap

gap = max(salaries_int)-min(salaries_int)

a = int(len(salaries_int)//2)

sum = 0

for c in salaries_int:
    sum += c

average = round(sum/len(salaries_int))

# Result
if len(salaries) % 2 == 1:
    print(f"Median: {round(salaries_int[a])}")
else:
    print(f"Median: {round((salaries_int[a-1]+salaries_int[a])/2)}")

print(f"Average: {average}")

print(f"Gap: {gap}")
