# Read and print positive numbers

print("Enter positive integers. End by giving a negative integer.")

lst = []
n = 1
i = 1

while n > 0:
    n = int(input("Integer "+str(i)+": "))
    if n > 0:
        lst.append(n)
    i += 1

print("\nNumber of positive integers:", len(lst))
print("Positive numbers:", lst)
