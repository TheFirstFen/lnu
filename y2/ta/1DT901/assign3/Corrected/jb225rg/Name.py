from dataclasses import dataclass


@dataclass
class Name():
    First_name: str = ""   # attributes
    Last_name: str = ""

    # full name as string
    def to_string(self):
        s = self.First_name + " " + self.Last_name
        return s

    # first name
    def get_first(self):
        return self.First_name

    # last name
    def get_last(self):
        return self.Last_name

    # set first name for new Name
    def set_first(self, first):
        self.First_name = first

    # set last name for new Name
    def set_last(self, last):
        self.Last_name = last

    # first letter and last name
    def short_name(self):
        first = self.get_first()  # first name
        letters = []
        for i in first:
            letters.append(i)  # letters of first name
        # first letter in list and last name
        s_name = letters[0] + ". " + self.Last_name
        return s_name
