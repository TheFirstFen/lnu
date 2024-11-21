print("Please provide three integers, A, B, C.")

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

max_num = a

if (b > max_num):
    max_num = b

if (c > max_num):
    max_num = c

print("The largest number is:", max_num)
