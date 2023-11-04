from dataclasses import dataclass


@dataclass
class Name:
    first_name: str = ""
    last_name: str = ""

    def get_first(self):
        s = self.first_name
        return s

    def get_last(self):
        s = self.last_name
        return s

    def to_string(self):
        s = ""
        # If not an emty str
        if self.first_name:
            # Append first_name
            s += self.first_name + " "
        if self.last_name:
            s += self.last_name
        return s

    def set_first(self, first_name):
        self.first_name = first_name
        return self

    def set_last(self, last_name):
        self.last_name = last_name
        return self

    def get_short_name(self):
        # if it has first/last name
        if self.first_name and self.first_name:
            # Take the first character uppercase.
            s = self.first_name[0].upper() + ". "
            # and first character in last_name uppercase
            s += self.last_name[0].upper()
            # follow by 3 character
            s += self.last_name[1:4]
            return s
        elif self.first_name and not self.last_name:
            return self.first_name[0].upper()
        elif self.last_name and not self.first_name:
            # last name only
            return " " + self.last_name[0].upper() + self.last_name[1:4]
        else:
            # If it doesnt have first/last name return None
            return None
