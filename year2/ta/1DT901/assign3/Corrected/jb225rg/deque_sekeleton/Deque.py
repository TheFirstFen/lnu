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
        if self.head is None:  # if no first node, add it
            self.head = new
            self.tail = self.head  # first element is also last
        else:
            self.tail.nxt = new  # next after tail is new node
        self.tail = new  # new node is now tail
        self.size += 1  # size increase

    # Returns a string representation of the current deque content
    def to_string(self):
        s = "{ "  # start string
        node = self.head
        while node is not None:  # go through entire lsit
            s += str(node.value) + " "  # add value to sting
            node = node.nxt
        s += "}"
        return s  # return string

    # Add element n as first entry in deque
    def add_first(self, n):
        new = Node(n, None)  # new node
        if self.head is None:  # if empty new is head and tail
            self.head = new
            self.tail = new
        else:
            tmp = self.head  # store current head in temporary variable
            self.head = new  # new node is head
            self.head.nxt = tmp  # the one after new is old head
        self.size += 1  # size increade

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.head is None:  # if empty
            print("You cannot acces an empty queue.")
        else:
            v = self.tail.value
            return v  # return tail value

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.head is None:  # if empty
            print("You cannot acces an empty queue.")
        else:
            v = self.head.value
            return v  # retirn head value

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        first = None
        if self.head is None:  # if empty
            print("You cannot remove an element fron an empty queue")
        elif self.size == 1:  # if only one node
            first = self.get_first()  # value of node
            self.head = None  # remove it
            self.tail = None
            self.size -= 1  # size recrease
        else:
            first = self.get_first()  # get value of first node
            self.head = self.head.nxt  # skip it
            self.size -= 1
        return first

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        last = None
        if self.head is None:  # if empty
            print("You cannot remove a element fron an empty queue")
        elif self.size == 1:  # if one node
            last = self.get_last()
            self.tail = None  # remove it
            self.head = None
            self.size -= 1
        else:
            last = self.get_last()
            pos = self.head  # position
            while pos.nxt != self.tail:  # until we reach before tail
                pos = pos.nxt  # move to next node
            pos.nxt = None  # remove ir
            self.tail = pos  # node before last one is new tail
            self.size -= 1
        return last
