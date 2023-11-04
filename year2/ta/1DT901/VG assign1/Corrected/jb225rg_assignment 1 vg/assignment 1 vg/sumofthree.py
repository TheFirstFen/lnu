num = int(input("Provide a three digit number: ")) #input of three digit number

digit_1 = num//100 #calculation of the first number

digit_3 = num%10 #Calculation of the last number

num = num//10 #removing the last digit
digit_2 = num%10 #modulus to get the last digigt of the now two digit number

digits = digit_1 + digit_2 + digit_3 #adding the digits together

print(f"The sum of the digits in that number is {digits}") #printing the results