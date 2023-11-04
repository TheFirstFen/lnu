#Ask the user for a three digit number
num = int(input("Provide a three digit number: "))

#Split into three digits
last = num % 10
num = num // 10

middle = num % 10
num = num // 10

first = num % 10

#calculate the sum
sum = last + middle + first

#Print results
print(f"Sum of digits: {sum}")