var = int(input("Enter a three digit number:  "))
digit_1 = (var//10)//10
digit_2 = (var//10)%10
digit_3 = var%10
total = digit_1 + digit_2 + digit_3
print("The total is ",total)