from dataclasses import dataclass


@dataclass
class MultiDisplay:
    message: str = ""
    count: int = 0

    def set_message(self, msg):
        self.message = msg

    def set_count(self, c):
        self.count = c

    def to_string(self):
        return f"Message: {self.message}, Count: {self.count}"

    def display(self):
        for i in range(self.count):
            print(self.message)

    def set_display(self, msg, c):
        self.message = msg
        self.count = c

    def get_message(self):
        return self.message
