from dataclasses import dataclass


@dataclass
class Name:
    first_name: str = ""
    last_name: str = ""

    def get_first(self):
        return self.first_name

    def get_last(self):
        return self.last_name

    def set_first(self, name):
        self.first_name = name

    def set_last(self, name):
        self.last_name = name

    def to_string(self):
        return self.first_name + " " + self.last_name

    def short_name(self):
        first = self.first_name[0]
        last = self.last_name[0: 4]
        return first + ". " + last
