from dataclasses import dataclass

# A data class representing a name


@dataclass
class Name:
    first: str = ""
    last: str = ""

    # Returns a string with first and last name
    def to_string(self):
        s = self.first + " " + self.last
        return s

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def set_first(self, fn):
        self.first = fn

    def set_last(self, ln):
        self.last = ln

    def get_short_name(self):
        return self.first[0] + ". " + self.last[0:4]
