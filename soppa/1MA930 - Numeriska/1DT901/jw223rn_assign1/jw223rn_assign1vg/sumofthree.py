number = int(input("Provide a three digit number: "))

#Calculating the number in each position and stores the value
first_num = number//100
second_num = (number//10)-(first_num * 10)
third_num = number - (first_num * 100) - (second_num * 10)

sum_of_three = first_num + second_num + third_num       #calculates the sum of the three digits previously aquired

print(sum_of_three)
