# Returns the median of the list
def median(sal_lst):
    if len(sal_lst) % 2 == 0:       # Checks if list has equal amount of values
        median1 = sal_lst[(len(sal_lst) // 2)]       # Stores one median
        median2 = sal_lst[(len(sal_lst) // 2) - 1]   # Stores the other median
        median = (median1 + median2) / len(sal_lst)  # Calcs the median of list
    else:
        median = sal_lst[(len(sal_lst) // 2)]   # Gets the median of the list
    return median


# Returns the average of the lsit
def average(sal_lst):
    n = 0           # Variable to store the sum of list
    for str in sal_lst:      # Checks each value in list and sums it together
        n = int(str) + n
    avg = n // len(sal_lst)  # Calculates the average of the list using the sum
    return avg


# Returns the gap between the first and last elemnt in the sorted list
def gap(sal_lst):
    gap = int(sal_lst[len(sal_lst) - 1]) - int(sal_lst[0])
    return gap


sal = input("Provide salaries: ")

sal_lst = sal.split()       # Converts input to a list

sal_lst.sort()              # Sorts the list by value low to high

# Stores each answer in desired variable
medi = median(sal_lst)
avg = average(sal_lst)
lst_gap = gap(sal_lst)

# Prints the answers
print(f"Median: {medi}")
print(f"Average: {avg}")
print(f"Gap: {lst_gap}")
