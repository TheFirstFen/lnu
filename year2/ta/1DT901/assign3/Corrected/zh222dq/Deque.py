from dataclasses import dataclass
from typing import Any

# A head-and-tail implementation of a deque using data classes


# Each node is an instance of class Node
@dataclass
class Node:
    value: int = None
    nxt: Any = None  # Any since Node not properly defined at this point


@dataclass
class Deque:
    head: Node = None      # First node in queue
    tail: Node = None      # Last node in queue
    size: int = 0

    # Add element n as last entry in deque
    def add_last(self, n):
        new = Node(n, None)
        if self.tail is None:
            self.head = self.tail = new
        else:
            self.tail.nxt = new
            self.tail = new
        self.size += 1

    # Returns a string representation of the current deque content
    def to_string(self):
        if self.head is None:
            return "{}"
        else:
            dict = "{ "
            node = self.head
            while node is not None:
                dict += str(node.value) + " "
                node = node.nxt
            dict += " }"
            return dict

    # Add element n as first entry in deque
    def add_first(self, n):
        new = Node(n, self.head)
        if self.head is None:
            self.tail = self.head = new
        else:
            new.nxt = self.head
            self.head = new
        self.size += 1

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.tail is None:
            return "You can't access an empty queue"
        else:
            node = self.tail
            return node.value

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.head is None:
            return "You can't access an empty queue"
        else:
            node = self.head
            return node.value

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.head is None:
            return "You can't access an empty queue"
        else:
            node = self.head
            self.head = node.nxt
            if self.head is None:
                self.tail = None
            self.size -= 1
            return node.value

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        if self.tail is None:
            return "You can't access an empty queue"
        elif self.head == self.tail:
            node = self.tail
            self.tail = self.head = None
            self.size = 0
        else:
            new_node = self.head
            while new_node.nxt != self.tail:
                new_node = new_node.nxt
            node = self.tail
            self.tail = new_node
            self.tail.nxt = None
            self.size -= 1
        return node.value
