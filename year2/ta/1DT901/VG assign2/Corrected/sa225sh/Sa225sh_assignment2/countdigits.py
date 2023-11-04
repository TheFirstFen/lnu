# increment the variable_counter by one if condition is satasfiad.
def counter():
    inp = input("Enter a large positive integer: ")
    odd, even, zero = 0, 0, 0
    for x in inp:
        if int(x) == 0:
            zero += 1
        elif int(x) % 2 == 0:
            even += 1
        else:
            odd += 1

    print(f"Zeros: {zero}\nOdd: {odd}\nEven: {even} ")


counter()
