
def mean(lst):
    return round(sum(lst)/len(lst))


def median(lst):
    # Sorted clone (not to affect input)
    clone = lst[::]
    clone.sort()

    sz = len(clone)
    if sz % 2 == 1:  # Odd size ==> pick mid element
        return clone[sz//2]
    else:         # Even size ==> mean of two mid elements
        mid = sz//2
        pair = clone[mid-1:mid+1]
        return mean(pair)


def gap(lst):
    return max(lst)-min(lst)


# Program start
# Convert space separated sting into integer list
text = input("Provide salaries: ")
words = text.split()
salaries = [int(w) for w in words]

# First example - odd size
# salaries = [21700,28200,26300,25100,22600,22800,19900]
print("\nMedian:", median(salaries))
print("Average:", mean(salaries))
print("Gap:", gap(salaries))

# First example - even size
# salaries = [22100,29800,27300,25400,23100,22300]
# print("Median:", median(salaries))
# print("Average:", mean(salaries))
# print("Gap:", gap(salaries))
