#read number of salaries (integers)
salaries = []
while True:
    salary = input("Enter a salary (or 'done' to finish): ")
    if salary == 'done': # breaks the code if the word done is typed in instead of a number
        break
    else:
        salary = int(salary)
        salaries.append(salary)

# Calculate the average salary
if len(salaries) > 0:
    total_salary = 0
    for s in salaries:
        total_salary += s
    average_salary = round(total_salary / len(salaries))
    print(f"Average Salary: {average_salary}")

    # Calculate the median salary
    salaries.sort()
    n = len(salaries)
    if n % 2 == 0:
        median_salary = round((salaries[n // 2 - 1] + salaries[n // 2]) / 2)
    else:
        median_salary = round(salaries[n // 2])
    print(f"Median Salary: {median_salary}")

    # Calculate the salary gap
    salary_gap = max(salaries) - min(salaries)
    print(f"Salary Gap: {salary_gap}")
else:
    print("No salaries provided.")
