n = int(input("Provide a three digit number:"))

# n%10 för att isolera siffran till höger
x = (n % 10)

# (n//10) % för att isolera siffran i mitten
y = (n // 10) % 10

# (n//100) % för att isolera siffran till vänster
z = (n // 100)

# sum för att addera de isolerade siffror
sum = x + y + z
round(sum)

print("Sum of digits:", sum)
