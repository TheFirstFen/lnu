# Deque.py
#
# Author: Samuel Berg
# Date: 05-Oct-2022

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

    # Add element n as first entry in deque
    def add_first(self, n):
        new = Node(n, None)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.head = Node(n, self.head)

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

    # Add element n as last entry in deque
    def add_last(self, n):
        new = Node(n, None)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            node = self.head
            while node.nxt is not None:
                node = node.nxt
            node.nxt = new
            self.tail = new

        self.size += 1

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.head is None:
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
        else:
            delete = self.head
            self.head = self.head.nxt
            self.size -= 1
            return delete.value

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        if self.head is None:
            print("You can't access an empty queue")
        elif self.size == 1:
            delete = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return delete.value
        else:   # size of list when emptying queue goes to zero one too early
            before = self.head
            while before.nxt.nxt is not None:
                before = before.nxt
            delete = before.nxt
            before.nxt = delete.nxt
            self.size -= 1
            return delete.value
