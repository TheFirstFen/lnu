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
        else:
            node = self.tail
            node.nxt = new
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
        new = Node(n, None)
        new.nxt = self.head
        self.head = new
        self.size += 1

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        last_node = self.tail
        last_val = last_node.value
        return last_val

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        first_node = self.head
        first_val = first_node.value
        return first_val

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.size == 1:
            self.head = None
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        first_val = self.get_first()
        self.head = self.head.nxt
        self.size -= 1
        return first_val

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        second_last = self.head
        last = self.head
        if self.size == 1:
            self.head = None
            self.size = 0
            return self.head
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        else:
            while last.nxt is not None:
                last = last.nxt
            while second_last.nxt is not last:
                second_last = second_last.nxt
            self.tail = second_last
            second_last.nxt = None
            self.size -= 1
        return last.value
