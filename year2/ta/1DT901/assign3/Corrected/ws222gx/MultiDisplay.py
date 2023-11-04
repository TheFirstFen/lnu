from dataclasses import dataclass


@dataclass
class MultiDisplay:
    message: str = ""
    count: int = 0

    def display(self):
        for i in range(self.count):
            print(self.message)

    def set_message(self, message):
        self.message = message

    def set_count(self, count):
        self.count = count

    def set_display(self, message, count):
        self.message = message
        self.count = count

    def to_string(self):
        return f"Message: {self.message}, Count: {self.count}"

    def get_message(self):
        return self.message
