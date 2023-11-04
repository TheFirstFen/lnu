# creat variables for each digit
a = 1000
b = 100
c = 10
d = 1

# loop until we get to the desired digit
while True:
    # add the digits to make a number
    digit = a + b + c + d
    # reverse the number
    reversed = int(str(digit)[::-1])
    # check if the reversed number is equal to the desired digit
    if reversed == digit * 4:
        print(digit)
        break
    # if not, increment the digits
    if d == 9:
        d = 1
        if c == 90:
            c = 0
            if b == 900:
                b = 0
                if a == 9000:
                    break
                a += 1000
            else:
                b += 100
        else:
            c += 10
    else:
        d += 1
