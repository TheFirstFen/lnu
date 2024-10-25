n = int(input("Enter a large positive integer: "))

zeros, odd, even = 0, 0, 0

# checks if the number is a positive integer
if n > 0:
    # goes through each number
    for num in str(n):
        # checks if the number is zero, odd or even
        if int(num) == 0:
            zeros += 1
        elif int(num) % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Zeros:", zeros)
    print("Odd:", odd)
    print("Even:", even)
else:
    print("Number is not a positive integer")
