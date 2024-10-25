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
        if self.tail is None:
            self.tail = new
            self.head = new
        else:
            self.tail.nxt = new
            self.tail = new
        self.size += 1

    # Returns a string representation of the current deque content
    def to_string(self):
        s = "{ "
        node = self.head
        while node is not None:
            s += str(node.value) + " "
            node = node.nxt
        s += "}"
        return s

    # Add element n as first entry in deque
    def add_first(self, n):
        new = Node(n)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.nxt = self.head
            self.head = new
        self.size += 1

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.

    def get_last(self):
        if self.tail is None:
            print("You can't access an empty queue")
            return None
        else:
            return self.tail.value

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        else:
            return self.head.value

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        elif self.head == self.tail:
            res = self.head.value
            self.head = None
            self.tail = None
            self.size -= 1
            return res
        else:
            res = self.head.value
            self.head = self.head.nxt
            self.size -= 1
            return res

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        if self.tail is None:
            print("You can't access an empty queue")
            return
        if self.size == 1:
            res = self.tail.value
            self.head = None
            self.tail = None
            self.size -= 1
            return res
        else:
            res = self.tail.value
            c_value = self.head
            while c_value.nxt != self.tail:
                c_value = c_value.nxt
            self.tail = c_value
            c_value.nxt = None
            self.size -= 1
            return res
