from dataclasses import dataclass


@dataclass
class MultiDisplay:
    message: str = ""
    count: int = 1

    # Välj meddelande
    def set_message(self, message):
        self.message = message

    # Välj hur många gånger det ska printas
    def set_count(self, count):
        self.count = count

    # Printar värdena som gavs
    def to_string(self):
        return f"Message: {self.message}, Count: {self.count}"

    # Printar meddelandet {count} gånger
    def display(self):
        for i in range(self.count):
            print(self.message)

    # Välj nya värden
    def set_display(self, message, count):
        self.message = message
        self.count = count
        self.display()

    # Lämnar tillbaka meddelandet
    def get_message(self):
        return self.message
