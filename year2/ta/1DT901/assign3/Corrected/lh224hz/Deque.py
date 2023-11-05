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

    def add_last(self, n):
        new_node = Node(n)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.nxt = new_node
            self.tail = new_node
        self.size += 1

    def to_string(self):
        s = "{ "
        node = self.head
        while node is not None:
            s += str(node.value) + " "
            node = node.nxt
        s += "}"
        return s

    def add_first(self, n):
        new_node = Node(n)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.nxt = self.head
            self.head = new_node
        self.size += 1

    def get_last(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        node = self.head
        while node.nxt is not None:
            node = node.nxt
        return node.value

    def get_first(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        return self.head.value

    def remove_first(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        removed_value = self.head.value
        self.head = self.head.nxt
        self.size -= 1
        return removed_value

    def remove_last(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        if self.head.nxt is None:
            removed_value = self.head.value
            self.head = self.tail = None
        else:
            before = self.head
            while before.nxt.nxt is not None:
                before = before.nxt
            removed_value = before.nxt.value
            before.nxt = None
            self.tail = before
        self.size -= 1
        return removed_value
