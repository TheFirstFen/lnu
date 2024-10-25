import Character

# Creating a character.
tiin = Character.character("Saesee Tiin", "Iktotchi", "Iktotch")
# printing that character.
print(tiin.to_string())

# Creating a variable for a character
solo = Character.character()
# Assigning a name to the character
solo.name = 'Han Solo'
# Assigning a kind to the character
solo.kind = 'Human'
# Assigning a planet to the character
solo.planet = 'Corellia'

# Print the full character
print(solo.to_string())
