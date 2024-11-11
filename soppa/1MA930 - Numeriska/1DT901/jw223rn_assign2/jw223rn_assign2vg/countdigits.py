# Function returns true if value is even
def is_even(x):
    return x % 2 == 0


num = input("Enter a large positive integer: ")

# Creating variables
even = 0
odd = 0
zero = 0

# for loop that checks each number in input and adds 1 to the correct variable
for i in range(len(num)):
    if int(num[i - 1]) == 0:
        zero += 1
    elif is_even(int(num[i - 1])):
        even += 1
    else:
        odd += 1

# Prints the number of zeros, evens and odds
print(f"Zeros: {zero}")
print(f"Odd: {odd}")
print(f"Even: {even}")
