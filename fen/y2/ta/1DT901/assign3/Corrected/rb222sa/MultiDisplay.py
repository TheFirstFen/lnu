from dataclasses import dataclass


@dataclass
class MultiDisplay:
    def set_message(self, message):
        self.message = message

    def set_count(self, count):
        self.count = count

    def to_string(self):
        return f"Message: {self.message}, Count: {self.count}"

    def display(self):
        for i in range(0, self.count):
            print(self.message)

    def set_display(self, message, count):
        self.message = message
        self.count = count
        for i in range(0, self.count):
            print(self.message)

    def get_message(self):
        return self.message
