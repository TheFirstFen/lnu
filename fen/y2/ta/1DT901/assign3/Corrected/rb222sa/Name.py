
from dataclasses import dataclass


@dataclass
class Name:
    firstname: None
    lastname: None

    def __init__(self, firstname=None, lastname=None):
        self.firstname = firstname
        self.lastname = lastname
        return

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def to_string(self):
        return f'{self.firstname} {self.lastname}'

    def get_first(self):
        return self.firstname

    def get_last(self):
        return self.lastname

    def set_first(self, firstname):
        self.firstname = firstname

    def set_last(self, lastname):
        self.lastname = lastname

    def get_short_name(self):
        return f'{self.firstname[:1]}. {self.lastname[:4]}'
