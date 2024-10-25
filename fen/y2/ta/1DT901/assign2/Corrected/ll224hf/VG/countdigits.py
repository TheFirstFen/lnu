# function to find amount of even, odd or amount of zero numbers
def find_out(number):
    zero = 0
    even = 0
    odd = 0
    for i in number:
        if int(i) == 0:
            zero += 1
        elif int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return zero, even, odd


# input to check, turn into string
number = str(input("Enter a large positive integer: "))

# run function to find out
zero, even, odd = find_out(number)

# print results
print(f"Zeros: {zero} \nOdd: {odd} \nEven: {even}")
