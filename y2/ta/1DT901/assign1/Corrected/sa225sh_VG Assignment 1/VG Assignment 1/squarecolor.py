
def square():
    n = input("Enter a chess square identifier ")
    list = ["a","c","e","g"]
    if n[0] in list:
        if int(n[1])% 2 == 0:
            print(f"{n} is white")
        else:
            print(f"{n} is black")
    else:
        if int(n[1])% 2 == 0:
            print(f"{n} is black")
        else:
            print(f"{n} is white")
square()