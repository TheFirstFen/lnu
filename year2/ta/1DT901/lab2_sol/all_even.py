# Add even numbers between 0 and 100

# Using for statement (Alternative 1)
sum = 0
for i in range(0, 101, 2):
    sum = sum + i
print("\nSum of the 100 first even numbers using for is:", sum)

# Using while statement (Alternative 2)
n = 0
sum = 0
while n <= 100:
    sum = sum + n
    n = n + 2
print("\nSum of the 100 first even numbers using while is:", sum)
