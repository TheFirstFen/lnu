# simple_star_wars_character.py
#
# Author: Samuel Berg
# Date: 03-Oct-2022

import Character

# Main code
#  Creates a character called Saesee Tiin
tiin = Character.Character('Saesee Tiin', 'Iktotchi', 'Iktotch')
print(tiin.to_string())

#  Creates an empty character later filled with Han Solo
solo = Character.Character()
solo.set_name('Han Solo')
solo.set_kind('Human')
solo.set_planet('Corellia')
print(solo.to_string())
