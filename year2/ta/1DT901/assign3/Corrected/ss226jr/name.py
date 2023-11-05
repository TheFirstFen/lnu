from dataclasses import dataclass


@dataclass
class Name:
    first: str = ""
    last: str = ""

    def to_string(self):
        return f"{self.first} {self.last}"

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def set_first(self, first_name):
        self.first = first_name

    def set_last(self, last_name):
        self.last = last_name

    def get_short_name(self):
        return f"{self.first[0]}. {self.last[:4]}"
