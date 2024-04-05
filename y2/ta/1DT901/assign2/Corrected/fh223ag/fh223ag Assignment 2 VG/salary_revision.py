# Ask the user for salaries
salaries = input("Provide salaries: ")

# Split the string into a list and convert to ints
salary_lst = salaries.split(" ")
salary_lst = [int(i) for i in salary_lst]


# calculate average and round
average = 0
total = 0
for i in salary_lst:
    total += i
average = total / len(salary_lst)
average = round(average)


# Sort list
salary_lst.sort()

# Calculate median
median = 0
half_length = int(len(salary_lst) / 2)
if len(salary_lst) % 2 != 0:
    median = round(salary_lst[half_length])
else:
    median_lower_num = round(salary_lst[half_length - 1])
    median_upper_num = round(salary_lst[half_length])
    median = round((median_lower_num + median_upper_num) / 2)

# Calculate Gap
gap = round(salary_lst[len(salary_lst) - 1] - salary_lst[0])

# Print results
print(f"Median: {median}")
print(f"Average: {average}")
print(f"Gap: {gap}")
