# store a number input from the user
input_num = input("Enter a large positive integer: ")

# creat a counter variable to store the number of zeros, odd and even
zeros = 0
odd = 0
even = 0

# loop through the input number and check if it is a zero, odd or even
for i in range(len(input_num)):
    if int(input_num[i]) == 0:
        zeros += 1
    elif int(input_num[i]) % 2 == 0:
        even += 1
    else:
        odd += 1

# print the results
print(f"Zeros: {zeros}\nOdd: {odd}\nEven: {even}")
