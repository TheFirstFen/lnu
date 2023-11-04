# For any given positive integer n (read from the keyboard)
# print all odd numbers up to n.

n = int(input("Enter a positive integer: "))

print("Odd numbers using for: ", end="")
for i in range(1, n+1, 2):
    print(i, "", end="")
print()

print("Odd numbers using while: ", end="")
i = 1
while i <= n:
    print(i, "", end="")
    i = i + 2
print()
