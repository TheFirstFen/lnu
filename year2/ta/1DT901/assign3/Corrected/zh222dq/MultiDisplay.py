from dataclasses import dataclass


@dataclass
class MultiDisplay:
    message: str = ""  # Stores the message string
    count: int = 0  # Stores the count of times to display the message.

    # Sets the message attribute.
    def set_message(self, n):
        self.message = n

    # Sets the count attribute.
    def set_count(self, n):
        self.count = n

    # Returns a string representation.
    def to_string(self):
        return f"Message: {self.message}, Count: {self.count}"

    # Prints the message 'count' times.
    def display(self):
        i = 0
        while i < self.count:
            print(self.message)
            i += 1

    # Sets message and count attributes, then displays the message.
    def set_display(self, message, count):
        self.set_message(message)
        self.set_count(count)
        self.display()

    # Returns the current message.
    def get_message(self):
        return self.message
