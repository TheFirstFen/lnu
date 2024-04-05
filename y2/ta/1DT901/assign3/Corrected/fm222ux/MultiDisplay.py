# Import dataclass
from dataclasses import dataclass


# Class Multidisplay
@dataclass
class MultiDisplay:
    message: str = ""
    count: int = 0

    def set_message(self, new_message):
        self.message = new_message

    def set_count(self, new_count):
        self.count = new_count

    def to_string(self):
        return f"Message: {self.message}, Count: {self.count} "

    def display(self):
        for i in range(self.count):
            print(self.message)

    def set_display(self, new_message, new_count):
        self.message = new_message
        self.count = new_count
        self.display()

    def get_message(self):
        return self.message

    def get_count(self):
        return self.count
