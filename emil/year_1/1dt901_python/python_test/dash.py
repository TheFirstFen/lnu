def add_dash(n):
    s = len(n)
    new_str = ""
    for i in n:
        if len(new_str) == 2*s-2:
            new_str += i
        else:
            new_str += i + "-"
    return new_str


n = str(input("Enter a string here: "))
print("old sentens: ", n)
print("The new string is:", add_dash(n))
