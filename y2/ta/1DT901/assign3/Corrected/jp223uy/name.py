from dataclasses import dataclass


@dataclass
class Name:
    first_name: str = ""
    last_name: str = ""

    def get_name(self):  # Return the input with a space
        return self.first_name + " " + self.last_name

    def get_first(self):  # Return input for first name
        return self.first_name

    def get_last(self):  # Return input for last name
        return self.last_name

    def set_first(self, name):  # Refer to main even with new name
        self.first_name = name

    def set_last(self, name):  # Same as set_first
        self.last_name = name

    # Return first letter and first 3 letters, sep with .
    def short_name(self):
        return self.first_name[0] + ". " + self.last_name[0:4]
