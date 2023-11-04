def revision(salaries):
    if not salaries:
        print("No valid salaries entered.")
        return

    salaries_sorted = sorted(salaries)
    length = len(salaries)

    if length % 2 == 1:  # Odd number of elements
        median = salaries_sorted[length // 2]
    else:  # Even number of elements
        mid_index_1 = length // 2
        mid_index_2 = mid_index_1 - 1
        value = salaries_sorted[mid_index_1] + salaries_sorted[mid_index_2]
        median = value / 2

    average = round(sum(salaries) / length)
    lowest_payed = min(salaries)
    highest_payed = max(salaries)
    gap = highest_payed - lowest_payed
    salaries_str = ', '.join(map(str, salaries))

    print(f"Provided salaries: {salaries_str}\nMedian: {median}\nAverage:\
{average}\nGap: {gap}")


def user_input():
    salaries = []
    salary_str = input("Enter salaries separated by white spaces\
(press enter when done): ")

    salary_list = salary_str.split()
    for salary in salary_list:
        try:
            salary = int(salary)
            salaries.append(salary)
        except ValueError:
            print(f"Invalid input: '{salary}' is not a valid salary.")
    return revision(salaries)


user_input()
