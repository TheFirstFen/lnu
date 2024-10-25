from dataclasses import dataclass


@dataclass
class Name:
    first_name: str = ""
    last_name: str = ""

    def to_string(self):
        return self.first_name + " " + self.last_name

    def get_first(self):
        return self.first_name

    def get_last(self):
        return self.last_name

    def get_short_name(self):
        return self.first_name[0] + ". " + self.last_name[0:4]

    def set_first(self, name):
        self.first_name = name

    def set_last(self, name):
        self.last_name = name
