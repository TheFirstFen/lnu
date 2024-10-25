from dataclasses import dataclass


# Creating a dataclass called character.
@dataclass
class character:
    # Creating three fields.
    name: str = ""
    kind: str = ""
    planet: str = ""

    # Made for simple star wars.
    # Creating a def called to_string.
    def to_string(self):
        # variable made to set the fields to the respective part.
        to_str = (
            f" {self.name}"
            f" is a(n) {self.kind}"
            f" from {self.planet}"
            )
        return to_str

    # Made for reading starwars.
    # Creating a def called for_reading
    def for_reading(self):
        # variable made to set the fields to the respective part.
        prt = (
            f"{self.name}"
            f" {self.kind}"
            f" {self.planet}"
        )
        return prt
