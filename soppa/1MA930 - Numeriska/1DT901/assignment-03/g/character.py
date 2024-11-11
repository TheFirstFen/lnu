from dataclasses import dataclass


@dataclass
class Character:
    name: str = ""
    kind: str = ""
    planet: str = ""

    def set_name(self, name):
        self.name = name

    def set_kind(self, kind):
        self.kind = kind

    def set_planet(self, planet):
        self.planet = planet

    # Convert fields to a string
    def to_string(self):
        return f"{self.name} is a(n) {self.kind} from {self.planet}"

    # Convert fields to rows
    def to_row(self):
        return f"{self.name}\t\t{self.kind}\t\t{self.planet}"
