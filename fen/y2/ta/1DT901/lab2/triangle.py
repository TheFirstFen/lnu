
n = int(input("Enter an odd positive integer: "))

if n > 0 and n % 2 == 1:
    print("\nRight-Angled Triangle:")
    for i in range(n):
        space = i*" "
        stars = (n-i)*"x"
        print(space+stars)

    print("\nIsoceles Triangle:")
    for i in range(1, n+1, 2):
        space = (n-i)//2*" "
        stars = i*"x"
        print(space+stars)
    print()
else:
    print("The number must be positive and odd!")
