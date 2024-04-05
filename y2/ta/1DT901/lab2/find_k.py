# For a given n,
# - find smallest k such that 1+3+5+...+k > n
# - find largest k such that 0+2+4+6+8+...+k < n

n = int(input("Enter a positive integer: "))
print()   # Add empty line

if n < 1:
    print("You must enter a positive number!")
else:
    # Smallest k idea: Keep adding while sum <= n
    sum = 0
    k = -1
    while sum <= n:
        k = k + 2
        sum = sum + k
    print(k, "is the smallest k such that 1+3+5+...+k >", n)

    # Largest k idea: Find smallest k such that sum >= n
    # and subtract two from k
    sum = 0
    k = 0
    while sum < n:
        k += 2
        sum += k
    print(k-2, "is the largest k such that 0+2+4+...+k <", n)
