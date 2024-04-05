from dataclasses import dataclass


@dataclass
class Name:
    first: str = ""  # Initialize first name as an empty string.
    last: str = ""  # Initialize last name as an empty string.

    # Combines first and last names into a full name string
    def to_string(self):
        return f"{self.first} {self.last}"

    # Returns the first name
    def get_first(self):
        return self.first

    # Returns the last name
    def get_last(self):
        return self.last

    # Sets the first name and returns it
    def set_first(self, f):
        self.first = f
        return self.first

    # Sets the last name and returns it
    def set_last(self, la):
        self.last = la
        return self.last

    # Returns the first initial and first four letters of last name
    def get_short_name(self):
        first = self.first[0]
        last = self.last[0:4]
        return (f"{first}. {last}")
