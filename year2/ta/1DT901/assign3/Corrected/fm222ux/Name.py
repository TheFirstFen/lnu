# Import dataclass
from dataclasses import dataclass


# Create class Name
@dataclass
class Name:
    first: str = ""
    last: str = ""

    def to_string(self):
        return self.first + " " + self.last

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def set_first(self, new_name):
        self.first = new_name

    def set_last(self, new_name):
        self.last = new_name

    def get_short_name(self):
        name1 = self.first[0]
        name2 = self.last[0:4]

        short = f"{name1}. {name2}"
        return short
