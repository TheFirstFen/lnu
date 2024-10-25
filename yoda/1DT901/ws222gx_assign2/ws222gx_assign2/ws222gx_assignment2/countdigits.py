n = input("Enter a large positive integer: ")

zeros, odd, even = 0, 0, 0

# checks if the number is a positive integer

if int(n) > 0:
    # goes through each number
    for num in n:
        # checks if the number is zero, odd or even

        if num == "0":
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
