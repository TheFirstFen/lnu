num = int(input("Insert 3 digit number: "))


num1 = num//100

num2 = (num //10) %10

num3 = num %10

sum = num1 + num2 + num3

print(sum)