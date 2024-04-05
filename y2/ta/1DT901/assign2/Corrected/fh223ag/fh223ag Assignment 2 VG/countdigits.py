# Create list for zero, odd and even
zeros_lst = []
odd_lst = []
even_lst = []

# Ask the user for a positive number
user_number = int(input("Enter a large positive integer: "))

# Make sure that the input is positive or ask again
while user_number < 1:
    user_number = int(input("Enter a large positive integer: "))

# convert user_number to string
user_number = str(user_number)

# go through the integer and check if the number is zero, odd or even
for i in range(0, len(user_number)):
    if int(user_number[i]) == 0:
        zeros_lst.append(user_number[i])
    elif int(user_number[i]) % 2 == 0:
        even_lst.append(user_number[i])
    else:
        odd_lst.append(user_number[i])

# print results
print(f"\n\nZeros: {len(zeros_lst)}")
print(f"Odd: {len(odd_lst)}")
print(f"Even: {len(even_lst)}")
