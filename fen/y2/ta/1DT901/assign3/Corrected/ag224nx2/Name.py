from dataclasses import dataclass


@dataclass
class Name:
    FirstName: str = ''
    SecondName: str = ''

    def to_string(self):
        namnet = f'{self.FirstName} {self.SecondName}'
        return namnet

    def get_first(self):
        first_name = f'{self.FirstName}'
        return first_name

    def get_last(self):
        last_name = f'{self.SecondName}'
        return last_name

    def set_first(self, new):
        self.FirstName = new
        return self.FirstName

    def set_last(self, new2):
        self.SecondName = new2
        return self.SecondName

    def get_short_name(self):
        short = self.FirstName[0] + '.' + self.SecondName
        return short
