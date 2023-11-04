
# First variant using modules and integer divions
n = int(input("Provide a three digit number: "))

last = n % 10
n = n // 10    # Remove last digit

mid = n % 10
n = n // 10    # Remove last didgit

first = n
print("Sum of digits: ", first+mid+last)

# Second variant treating input as a string
str = input("\nProvide a three digit number: ")
first = int(str[0])
mid = int(str[1])
last = int(str[2])
print("Sum of digits: ", first+mid+last)
