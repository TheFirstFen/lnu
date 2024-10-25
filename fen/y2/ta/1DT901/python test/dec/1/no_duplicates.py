
print("Provide integers and stop with a duplicate element\n")

count = 1
flag = True
lst = []
while flag:
    n = int(input(f"Number {count}: "))
    if n in lst:
        flag = False
    else:
        lst.append(n)
        count += 1

print("\nAll numbers")
for n in lst:
    print(n)
