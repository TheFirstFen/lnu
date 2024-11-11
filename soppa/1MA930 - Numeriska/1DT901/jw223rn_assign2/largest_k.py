stop = int(input("Enter a positive integer: "))

k_u = 0

for k in range(0, stop, 2):
    k_u += k
    if k_u > stop:
        break
print(f"{k - 2} is the largest k such that 0+2+4+6+...+k < {stop}")
