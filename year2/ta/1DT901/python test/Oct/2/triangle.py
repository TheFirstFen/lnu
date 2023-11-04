n = int(input("Enter a positive integer: "))

if n < 1:
    print("It must be a positive number!")
    exit()

# Print upper half
for i in range(1, n+1):
    sp = (n-i) * " "
    st = i * "*"
    print(sp+st)

# Print lower half
for i in range(n-1, 0, -1):
    sp = (n-i) * " "
    st = i * "*"
    print(sp+st)
