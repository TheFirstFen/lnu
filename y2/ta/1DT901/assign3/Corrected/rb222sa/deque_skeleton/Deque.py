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
        if self.head is None:
            self.head = new
            self.tail = self.head
            self.size = 1
        else:
            self.tail.nxt = new
            self.tail = self.tail.nxt
            self.size += 1
        pass

    # Returns a string representation of the current deque content
    def to_string(self):
        string = "{ "
        current_node = self.head
        while current_node is not None:
            string += str(current_node.value) + " "
            current_node = current_node.nxt
        string += "}"
        return string

    # Add element n as first entry in deque
    def add_first(self, n):
        new = Node(n, None)
        if self.head is None:
            self.head = new
            self.tail = self.head
            self.size = 1
        else:
            new.nxt = self.head
            self.head = new
            self.size += 1
        pass

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.size == 0:
            return None
        else:
            return self.tail.value
        pass

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.size == 0:
            return None
        else:
            return self.head.value


    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            value = self.head
            self.head = None
            self.tail = None
            self.size = 0
        else:
            value = self.head
            self.head = self.head.nxt
            self.size -= 1
        return value.value

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    # Figure out next to last position and remove last with nxt = None
    def remove_last(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            value = self.tail
            self.head = None
            self.tail = None
            self.size = 0
        else:
            value = self.tail
            position = self.head
            while position.nxt is not self.tail:
                position = position.nxt
            self.tail = position
            self.tail.nxt = None
            self.size -= 1
        return value.value
