user_input = int(input("Enter a positive integer: "))

# for loop
print("Odd numbers using for: ", end="")
for num in range(1, user_input+1, 2):
    print(num, end=" ")

# while loop
num = 1
print("\nOdd numbers using while: ", end="")
while num <= user_input:
    print(num, end=" ")
    num += 2
