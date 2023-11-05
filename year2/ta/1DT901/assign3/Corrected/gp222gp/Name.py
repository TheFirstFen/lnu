from dataclasses import dataclass


@dataclass
class Name:
    first_name: str = ''
    last_name: str = ''

    def to_string(self):
        fullname = f"{self.first_name} {self.last_name}"
        return fullname

    def get_first(self):
        firstname = f"{self.first_name}"
        return firstname

    def get_last(self):
        lastname = f"{self.last_name}"
        return lastname

    def set_first(self, first_name):
        self.first_name = first_name

    def set_last(self, last_name):
        self.last_name = last_name

    def get_short_name(self):
        short_name = f"{self.first_name[0]} {self.last_name}"
        return short_name
