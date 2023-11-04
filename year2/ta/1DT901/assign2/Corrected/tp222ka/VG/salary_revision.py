

def average(lst):
    total = 0
    for n in lst:
        total += int(n)
    avg = total / len(lst)  # Calculate the average
    return round(avg)  # Round to the nearest integer and return


# Calculate gap, maximum and minimum values
def gap(lst):
    lst = sorted(lst)  # Sort the list in ascending order
    max_value = lst[len(lst)-1]  # last index
    min_value = lst[0]  # First index
    return int(max_value) - int(min_value)


def median(lst):
    lst = sorted(lst)  # Sort the list in ascending order
    middle = len(lst) // 2  # Middle index of the sorted list
    if len(lst) % 2 == 0:
        # Median as the average of the two middle elements
        median_val = (int(lst[middle - 1]) + int(lst[middle])) / 2
    else:
        # Median as the middle element
        median_val = int(lst[middle])
    return median_val


num = input("Provide salaries with space: ")
lst = num.split()  # Split the input string into a list of numbers

# Check if the list is not empty
if lst:
    print(f"Median: {median(lst)}\n"
          f"Average: {average(lst)}\n"
          f"Gap: {gap(lst)}\n")
else:
    print("Please provide a valid list of numbers.")
