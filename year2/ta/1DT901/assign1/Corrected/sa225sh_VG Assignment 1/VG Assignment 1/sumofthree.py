def sum_of_three():
    number = int(input("Provide a three digit number: "))
    sum = 0
    sum += number // 100
    sum += (number // 10) % 10
    sum += number % 10 
    print(f" sum of digits:{sum}")
sum_of_three()

