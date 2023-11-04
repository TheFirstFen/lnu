from dataclasses import dataclass


@dataclass
class Name:
    first: str = None
    last: str = None

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def get_short_name(self):
        first = self.get_first()
        last = self.get_last()
        short_name = first[0] + ". " + last
        return short_name

    def set_first(self, attribute1):
        self.first = attribute1

    def set_last(self, attribute2):
        self.last = attribute2

    def to_string(self):
        toString = ""
        first = self.get_first()
        last = self.get_last()
        toString += first + " " + last
        return toString
