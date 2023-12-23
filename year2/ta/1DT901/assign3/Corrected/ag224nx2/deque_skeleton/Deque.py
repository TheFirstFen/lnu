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
        newE = Node(n)
        if self.head is None:
            self.head = newE
            self.tail = newE

        elif self.tail is not None:
            self.tail.nxt = newE

        self.tail = newE
        self.size += 1

    # Returns a string representation of the current deque content

    def to_string(self):
        st = "{"
        node = self.head
        while node is not None:
            st += str(node.value) + " "
            node = node.nxt
        st += "}"
        return st

    # Add element n as first entry in deque
    def add_first(self, n):
        newE = Node(n, self.head)
        if self.size == 1:
            self.head = newE
            self.tail = newE
        else:
            self.head = newE
        self.size += 1

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.

    def get_last(self):
        node = self.tail
        if node is not None:
            return node.value
        elif node is None:
            print("You can't access an empty queue")
            return

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        txt = ''
        node = self.head
        if node is not None:
            txt += str(node.value)
            return txt
        elif node is None:
            print("You can't access an empty queue")
        return

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return
        value = self.head.value
        if self.size == 1:
            self.head = None
            self.tail = None
            return value
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
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
            return self.size
        else:
            cNode = self.head
            while cNode.nxt != self.tail:
                cNode = cNode.nxt
            remE = self.tail
            cNode.nxt = None
            self.tail = cNode
            self.size -= 1
            return remE.value
