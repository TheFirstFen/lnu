#Provide a three digit number: 456
#Sum of digits: 15

#collect input
n = int(input("Input a 3 digit number: "))

#seperate them into 3 different variables

#last digit
n3 = n%10

#middle digit
n2 = n%100
n2 = n2//10

#first digit
n1 = n//100

#add together
m = n1 + n2 + n3

#display result
print("The sum of the given 3 digits is:",m)