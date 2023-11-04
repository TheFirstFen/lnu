from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: int = None
    nxt: Any = None


@dataclass
class Deque:
    head: Node = None
    tail: Node = None
    size: int = 0

    def add_last(self, n):
        new_node = Node(value=n)
        if self.tail:
            self.tail.nxt = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.size += 1

    def to_string(self):
        if self.size == 0:
            return "{}"
        deq = self.head
        elements = []
        while deq is not None:
            elements.append(str(deq.value))
            deq = deq.nxt
        return "{" + " ".join(elements) + "}"

    def add_first(self, n):
        new_node = Node(value=n)
        if self.head:
            new_node.nxt = self.head
            self.head = new_node
        else:
            self.tail = self.head = new_node
        self.size += 1

    def get_last(self):
        if self.tail is not None:
            return self.tail.value
        else:
            return None

    def get_first(self):
        if self.head is not None:
            return self.head.value
        else:
            return None

    def remove_first(self):
        if self.size == 0:
            error = "The deque is Empty"
            return None, error
        elif self.size == 1:
            value = self.head.value
            self.head = self.tail = None
        else:
            value = self.head.value
            self.head = self.head.nxt
        self.size -= 1
        return value

    def remove_last(self):
        if self.size == 0:
            error = "The deque is Empty"
            return None, error
        elif self.size == 1:
            value = self.tail.value
            self.head = self.tail = None
        else:
            value = self.tail.value
            prev_node = self.head
            while prev_node.nxt != self.tail:
                prev_node = prev_node.nxt
            self.tail = prev_node
            self.tail.nxt = None
        self.size -= 1
        return value
