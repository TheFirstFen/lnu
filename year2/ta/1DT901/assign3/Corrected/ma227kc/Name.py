from dataclasses import dataclass


# To take arguments
@dataclass
# The class needed as instructed
class Name:
    # "" are need because an error would occur otherwise
    firstname: str = ""
    lastname: str = ""

    def get_first(self):
        return self.firstname

    def get_last(self):
        return self.lastname

    def to_string(self):
        return self.firstname + " " + self.lastname

    def set_first(self, first):
        self.firstname = first

    def set_last(self, last):
        self.lastname = last

    def get_short_name(self):
        return self.firstname[0] + ". " + self.lastname[0:4]
