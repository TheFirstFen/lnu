from dataclasses import dataclass


@dataclass
class MultiDisplay:

    def set_message(self, message):
        self.message = message

    def set_count(self, n):
        self.count = n

    def to_string(self):
        return f"Message: {self.message} Count: {self.count}"

    def display(self):
        print((self.message + "\n") * self.count)

    def set_display(self, variable, number):
        self.message = variable
        self.count = number
        print((variable + "\n") * number)

    def get_message(self):
        return f"{self.message}"
