from dataclasses import dataclass
from typing import Any

# A head-and-tail implementation of a deque using data classes


# Each node is an instance of class Node
@dataclass
class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self) -> bool:
        return self.head is None

    def add_first(self, value: Any) -> None:
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_last(self, value: Any) -> None:
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_first(self) -> Any:
        if self.is_empty():
            return None
        value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return value

    def remove_last(self) -> Any:
        if self.is_empty():
            return None
        value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return value

    def to_string(self) -> str:
        if self.is_empty():
            return "Deque is empty"
        current = self.head
        result = ""
        while current is not None:
            result += str(current.value) + " "
            current = current.next
        return result.strip()
