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
        new = Node(n)
        if self.size == 0:
            self.head = self.tail = new
        else:
            self.tail.nxt = new
            self.tail = new
        self.size += 1

    # Returns a string representation of the current deque content
    def to_string(self):
        lst = []
        hd = self.head
        while hd is not None:
            lst.append(str(hd.value))
            hd = hd.nxt
        return "{ " + " ".join(lst) + " }"

    # Add element n as first entry in deque
    def add_first(self, n):
        new = Node(n)
        if self.size == 0:
            self.head = self.tail = new
        else:
            new.nxt = self.head
            self.head = new
        self.size += 1

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        return self.tail.value

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        return self.head.value

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        value = self.head.value
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.nxt
        self.size -= 1
        return value

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        value = self.tail.value
        if self.size == 1:
            self.head = self.tail = None
        else:
            current = self.head
            while current.nxt != self.tail:
                current = current.nxt
            current.nxt = None
            self.tail = current
        self.size -= 1
        return value
