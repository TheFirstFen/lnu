n = int(input("Enter an integer larger than two: "))

if n < 3:
    print("Integer must be largar than 2!!!")
    exit()

print("x")
for i in range(2, n+1):
    if i == n:
        print("x"*i)
    else:
        print("x" + (i-2)*"o" + "x")
