from dataclasses import dataclass


@dataclass
class MultiDisplay:
    message: str = ""
    count: int = 0

    def set_message(self, message):
        # Set message from provide message
        self.message = message

    def set_count(self, count):
        # Set count from provide count
        self.count = count

    def to_string(self):
        s = self.message
        counts = self.count
        return f"message: {s}, counts: {counts}"

    def display(self):
        # display() # print-out look like print message * count
        message = self.message
        counts = self.count
        for i in range(counts):
            print(f"{message}")

    def set_display(self, message, count):
        # Set message and count directly
        self.message = message
        self.count = count

    def get_message(self):
        # return the current message
        message = self.message
        return message
