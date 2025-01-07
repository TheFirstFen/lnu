from QuadHash import QuadHash

hashing = QuadHash()
print("Checking for empty table")
print(hashing)

print()
words = ["hej", "jul", "nyår", "varför"]
for i in words:
    print(f"adding {i}", end=", ")
    hashing.add(i)

print("\nprinting table")
for i in hashing:
    print(i, end=" ")

print("\nchecking if hej is in the table")
print(hashing.contains("hej"))

print("\nchecking if 11 is in the table")
print(hashing.contains(11))


print("\nadding integers 0-9")
for i in range(10):
    hashing.add(i)

print("\nprinting table with __str__")
print(hashing)

print("printing table with iterator")
for i in hashing:
    print(i, end=" ")
