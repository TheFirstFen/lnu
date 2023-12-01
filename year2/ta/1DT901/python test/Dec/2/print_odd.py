print("Provide integers and stop with a negative")

count = 1
flag = True
lst = []
while flag:
    n = int(input(f"Number {count}: "))
    if n < 0:
        flag = False
    else:
        lst.append(n)
        count += 1

print("\nOdd numbers ")
for n in lst:
    if n % 2 == 1:
        print(n)
