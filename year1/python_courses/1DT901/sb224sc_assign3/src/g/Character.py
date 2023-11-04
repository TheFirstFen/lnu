# Character.py
#
# Author: Samuel Berg
# Date: 03-Oct-2022

class Character:
    '''__init__(self, name=None, kind=None, planet=None):
    If the Character class is called it will initialize
    a character object with the standard character values
    of None through out but if it is called with character
    specifics those will be assigned on initialization.
    '''
    def __init__(self, name=None, kind=None, planet=None):
        self.name = name
        self.kind = kind
        self.planet = planet

    def set_name(self, name):  # Can be called on character object to set name
        self.name = name

    def get_name(self):  # Can be called on character object to get name
        return self.name

    def set_kind(self, kind):   # Can be called on character object to set kind
        self.kind = kind

    def get_kind(self):  # Can be called on character object to get kind
        return self.kind

    def set_planet(self, planet):  # Can be called on character object to
        self.planet = planet       # set planet

    def get_planet(self):   # Can be called on character object to get planet
        return self.planet

    '''to_string():
    Can be called on character object to within a print statement to
    print out all of the character objects specifics
    '''
    def to_string(self):
        return f'{self.name} is a(n) {self.kind} from {self.planet}'
