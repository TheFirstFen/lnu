import random

n = random.randint(1, 100)
# print(n)

has_lost = True
for i in range(10):
    g = int(input(f"Guess {i+1}: "))
    if g < n:
        print("\tClue: Higher")
    elif g > n:
        print("\tClue: Lower")
    else:
        print("\tCorrect in only", i+1, "guesses - Excellent!")
        has_lost = False
        break
if has_lost:
    print("\nSorry, you lost! The magic number was", n)
