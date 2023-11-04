
# function to find median
def median(ints):

    # sort the list
    ints.sort()

    # find the middle in odds, kinda middle in even.
    middle = len(ints) // 2

    # for even lists of saleries
    if len(ints) % 2 == 0:
        return round((ints[middle - 1] + ints[middle]) / 2)
    # for odd salery lists
    else:
        return round(ints[middle])


# function to find average salery
def average(ints):

    # make variables for calculations
    repeats = 0
    total = 0

    # Go through all values and add them to total.
    # Add 1 to repeats every time you loop
    for i in ints:
        total += i
        repeats += 1

    # return the average, rounded.
    return round(total / repeats)


# function to find the gap
def gap(ints):

    # sort the list
    ints.sort()

    # take the last value and subtract the first, return rounded value.
    return round(ints[-1] - ints[0])


# From lecture 6.
text = input("Provide salaries: ")
words = text.split()
ints = [int(w) for w in words]

# print results using functions.
print(f"Median: {median(ints)}")
print(f"Average: {average(ints)}")
print(f"Gap: {gap(ints)}")
