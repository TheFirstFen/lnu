num = str(input("Write a number here: "))
even = 0
odd = 0
zero = 0
i = 0

while i < len(num):
    for s in num:
        if s == '2' or s == '4' or s == '6' or s == '8':
            even += 1
            i += 1
        elif s == '0':
            zero += 1
            i += 1
        else:
            odd += 1
            i += 1


print(f"Odd: {odd} \nEven: {even} \nZero: {zero}")
