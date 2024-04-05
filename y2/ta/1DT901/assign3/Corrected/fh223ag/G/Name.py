from dataclasses import dataclass


@dataclass
class Name:
    first_name: str = ""
    second_name: str = ""

    def to_string(self):
        full_name = self.first_name + " " + self.second_name
        return full_name

    def get_first(self):
        return self.first_name

    def get_last(self):
        return self.second_name

    def set_first(self, s):
        self.first_name = s
        return self.first_name

    def set_last(self, s):
        self.second_name = s
        return self.second_name

    def get_short_name(self):
        first_char = self.first_name[0]
        last = self.second_name[0: 4]
        short_name = first_char + ". " + last
        return short_name
