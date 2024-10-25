import itertools

# Create a list of all possible characters
# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chars = ['s', 'b', 'f']

# Generate all three letter combinations
combinations = itertools.product(chars, repeat=3)

# Open a file for writing
with open("combinations.txt", "w") as f:
    # Write each combination to the file
    for combination in combinations:
        f.write("".join(combination) + "\n")

print("All combinations written to combinations.txt")
