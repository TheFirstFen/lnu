square = input("Enter a chess square identifier (e.g. e5): ")

letter_to_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
letter_num = letter_to_num[square[0]]

number = int(square[1])

if (letter_num + number) % 2 == 0:
    color = "Black"
else:
    color = "white"

print(f"{square} is {color}.")




