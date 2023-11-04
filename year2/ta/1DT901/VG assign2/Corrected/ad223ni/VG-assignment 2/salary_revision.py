def calculate_median(salaries):
    sorted_salaries = sorted(salaries)
    n = len(sorted_salaries)
    if n % 2 == 0:
        mid1 = n // 2
        mid2 = mid1 - 1
        median = (sorted_salaries[mid1] + sorted_salaries[mid2]) // 2
    else:
        mid = n // 2
        median = sorted_salaries[mid]
    return median


def calculate_average(salaries):
    total = sum(salaries)
    average = total // len(salaries)
    return average


def calculate_salary_gap(salaries):
    min_salary = min(salaries)
    max_salary = max(salaries)
    gap = max_salary - min_salary
    return gap


salaries = input("Provide salaries: ").split()
salaries = [int(salary) for salary in salaries]
median = calculate_median(salaries)
average = calculate_average(salaries)
gap = calculate_salary_gap(salaries)

print("Median:", median)
print("Average:", average)
print("Gap:", gap)
