

def average(s_int):
    # compute sum

    # sum devided by number of elements
    avg = sum(s_int) / len(salary_int)
    avg = round(avg)

    return avg


def gap(s_int):
    # max minus min
    gap = max(s_int) - min(s_int)
    return gap


def median(s_int):
    # sort list
    salary_int.sort()
    n = len(salary_int)

    # if even number of elements, get average of 2 middle numbers
    if n % 2 == 0:
        median = (salary_int[n//2 - 1] + salary_int[n//2]) / 2
    else:  # is odd number of elements, get middle number
        median = salary_int[n//2]
    return median


salary = input("Provide salaries: ")

# get salaries into a list of ints
salary_str = salary.split()
salary_int = [int(n) for n in salary_str]

# printing resaults
print("Median:", median(salary_int))
print("Average:", average(salary_int))
print("Gap:", gap(salary_int))
