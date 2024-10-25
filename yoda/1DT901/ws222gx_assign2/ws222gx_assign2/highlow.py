import random


gen_num = random.randint(1, 100)
user_input = 1000
count = 1
correct = True
while user_input != gen_num:
    if count > 10:
        correct = False
        break

    user_input = int(input(f"Guess {count}: "))
    print("\tClue: Higher" if user_input < gen_num else "\tClue: Lower")
    count += 1


if correct:
    print(f"\tCorrect answer after only {count} guesses")
else:
    print(f"Game over the correct number was: {gen_num}")
