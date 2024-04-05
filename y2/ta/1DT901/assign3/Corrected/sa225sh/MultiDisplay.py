from dataclasses import dataclass


@dataclass
class MultiDisplay:
    message: str = None
    count: int = None

    def get_message(self):
        return self.message

    def get_count(self):
        return self.count

    def set_message(self, attribute1):
        self.message = attribute1

    def set_count(self, attribute2):
        self.count = attribute2

    def to_string(self):  # använda skapde getters för att nå värdet av self
        message = self.get_message()
        count = self.get_count()
        return f"Message: {message}, Count: {count}"

    def display(self):
        count = self.get_count()
        message = self.get_message()
        for s in range(count + 1):
            return message

    def set_display(self, attribute1, attribute2):
        self.set_message(attribute1)
        self.set_count(attribute2)
