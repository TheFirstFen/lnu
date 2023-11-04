#reads integer from user
number = int(input("Provide a three digit number: "))

#isolates the first number
first = number//100
number = number%100

#isolates the second number
second = (number//10)
number = number%10

#assigns the third number
third = number

#prints the sum of the individual three numbers
print("The sum is: ", first+second+third)