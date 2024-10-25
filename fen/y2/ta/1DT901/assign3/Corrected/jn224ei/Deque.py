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
            self.tail = new
        else:
            node = self.head
            while (node.nxt is not None):
                node = node.nxt
            node.nxt = new
            self.tail = node.nxt
        self.size += 1

    # Returns a string representation of the current deque content
    def to_string(self):
        nod = self.head
        txt = ""

        while nod is not None:
            txt += str(nod.value) + ' '
            nod = nod.nxt
        return txt

    # Add element n as first entry in deque
    def add_first(self, n):
        new = Node(n, self.head)
        if self.head is None:
            self.head = new
            self.tail = new
        self.head = new
        self.size += 1
    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.

    def get_last(self):
        if self.tail is not None:
            return self.tail.value
        else:
            return "There was no last value"

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.head is not None:
            return self.head.value
        else:
            return "There was no first value"

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.size > 1:
            temp = self.head.value
            self.head = self.head.nxt
            self.size -= 1
            return f"Removed {temp} from the Deque"
        elif self.size == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return f"Removed {temp} from the Deque"
        else:
            return "There was no first value"

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        if (self.head is None):
            return "There was no first value"
        elif (self.size == 1):
            temp = self.head.value
            self.head = None
            self.tail = None
            self.size -= 1
            return f"Removed {temp} from the Deque"
        else:
            nod = self.head
            temp = self.tail.value
            while nod.nxt is not self.tail:
                nod = nod.nxt
            nod.nxt = None  
            self.tail = nod

            self.size -= 1
            return f"Removed {temp} from the Deque"
