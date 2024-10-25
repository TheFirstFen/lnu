from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: int = None
    nxt: Any = None


@dataclass
class Deque:
    head: Node = None
    tail: Node = None
    size: int = 0

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, n):
        new = Node(n)
        if self.head == 0:
            self.head = new
            self.size = 1
            self.tail = self.head
        else:
            new.nxt = self.head
            self.head = new
            self.size += 1

    def to_string(self):
        s = "("
        node = self.head
        while node is not None:
            s += f"{node.value} "
            node = node.nxt
        s += ")"
        return s

    def add_last(self, n):
        new = Node(n)
        if self.size == 0:
            self.head = new
            self.size = 1
            self.tail = self.head
        else:
            self.tail.nxt = new
            self.tail = self.tail.nxt
            self.size += 1

    def get_last(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        else:
            return self.tail.value

    def get_first(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        else:
            return self.head.value

    def remove_first(self):

        if self.size == 0:
            print("You can't access an empty queue")
            return
        nod = self.head

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0

        else:
            self.head = self.head.nxt
            self.size -= 1
        return nod.value

    def remove_last(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return
        if self.size == 1:

            del self.head
            self.head = None
            self.tail = None
            self.size = 0
        else:
            prev = self.head
            last = self.tail
            while prev.nxt != last:
                prev = prev.nxt
            prev.nxt = None
            self.tail = prev
            self.size -= 1
            return last
