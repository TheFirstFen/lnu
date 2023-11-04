from dataclasses import dataclass


@dataclass
class Name:
    first_name: str = ""
    second_name: str = ""

    # Lämnar tillbaka det fulla namnet
    def to_string(self):
        return self.first_name + " " + self.second_name

    # Lämnar tillbaka förnamnet
    def get_first(self):
        return self.first_name

    # Lämnar tillbaka efternamnet
    def get_last(self):
        return self.second_name

    # Välj förnamn
    def set_first(self, first_name):
        self.first_name = first_name

    # Välj efternamn
    def set_last(self, second_name):
        self.second_name = second_name

    # Lämnar tillbaka "shortname"
    def get_short_name(self):
        return self.first_name[0] + ". " + self.second_name
