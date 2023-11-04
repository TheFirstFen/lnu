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
        new_node = Node(n)
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.nxt = new_node
            self.tail = new_node
        self.size += 1

    # Returns a string representation of the current deque content

    def to_string(self):
        i = '{ '
        node = self.head
        while node is not None:
            i += str(node.value) + ' '
            node = node.nxt
        i += '}'
        return i

    # Add element n as first entry in deque
    def add_first(self, n):
        new_node = Node(n)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.nxt = self.head
            self.head = new_node
        self.size += 1

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        else:
            node = self.head
            for i in range(self.size - 1):
                node = node.nxt
            return node.value

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
            removed_value = self.head.value
            self.head = self.tail = None
        else:
            removed_value = self.head.value
            self.head = self.head.nxt
        self.size -= 1
        return removed_value

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        elif self.head == self.tail:
            removed_value = self.head.value
            self.head = self.tail = None
            self.size -= 1
        else:
            node = self.head
            while node.nxt != self.tail:
                node = node.nxt
            removed_value = self.tail.value
            node.nxt = None
            self.tail = node
            self.size -= 1
        return removed_value
