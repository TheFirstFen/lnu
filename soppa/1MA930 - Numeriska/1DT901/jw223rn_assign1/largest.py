print("Please provide three integers A, B, C.")
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a > b and a > c:
    print(f"The largest number is: {a}")
elif b > a and b > c:
    print(f"The largest number is: {b}")
else:
    print(f"The largest number is: {c}")
