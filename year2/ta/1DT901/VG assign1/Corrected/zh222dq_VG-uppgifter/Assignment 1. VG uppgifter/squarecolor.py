n = input("Enter a chess square identifier (e.g. e5): ")

# De möjliga bokstäverna
list = ["a", "b", "c", "d", "e", "f", "g", "h"]

# Isolera bokstaven
n1 = str(n[0])

# Isolera siffran
n2 = int(n[1])

if n1 in ["a", "c", "e", "g"] and n2 % 2 == 0:
    print(f"{n} is white")
elif n1 in ["a", "c", "e", "g"] and n2 % 2 == 1:
    print(f"{n} is black")
elif n1 in ["b", "d", "f", "h"] and n2 % 2 == 0:
    print(f"{n} is black")
elif n1 in ["b", "d", "f", "h"] and n2 % 2 == 1:
    print(f"{n} is white")
else:
    print("Invalid")
