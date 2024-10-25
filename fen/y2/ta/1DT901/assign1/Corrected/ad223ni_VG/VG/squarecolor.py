
# Read the square identifier from the user
square = input("Enter a chess square identifier (e.g. e5): ")

# Extract the file (letter) and rank (integer) from the square identifier
file = square[0]
rank = int(square[1])

# Determine the color based on the file and rank
if (file in "aceg" and rank % 2 == 1) or (file in "bdfh" and rank % 2 == 0):
    color = "Black"
else:
    color = "White"

# Print the color of the square
print(square, "is", color)
