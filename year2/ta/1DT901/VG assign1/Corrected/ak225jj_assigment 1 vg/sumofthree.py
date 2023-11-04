
#Provide a three digit number 
n = int(input("Provide a three digit number: "))

#Count n1
n1 = n//100

#Count n2
nr2 = n%100
n2 = nr2//10

#Count n3
n3 = nr2%10

#give result
result = n1 + n2 + n3

print("Sum of digits: ", result)
