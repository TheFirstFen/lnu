salaries_string = input("Please provide salaries: ")
#  Turns salaries into a list
salaries = salaries_string.split()

#  Converts salaries to integers
for i in range(len(salaries)):
    salaries[i] = int(salaries[i])

#  sorts the salaries to then pick out highest and lowest salary
sorted_salaries = sorted(salaries)

highest = sorted_salaries[-1]
lowest = sorted_salaries[0]

gap = highest - lowest

middle = round(len(sorted_salaries)/2)
#  calculating the median
if (len(sorted_salaries) % 2 == 0):
    median1 = sorted_salaries[middle]
    median2 = sorted_salaries[middle-1]
    median = round((median1 + median2)/2)
else:
    median = sorted_salaries[middle-1]

#  calculating the average salary
average = round(sum(sorted_salaries)/len(sorted_salaries))

print("Median: ", median)
print("Average: ", average)
print("Gap: ", gap)
