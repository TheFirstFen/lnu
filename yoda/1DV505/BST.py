from dataclasses import dataclass
from typing import Any
from typing_extensions import Self

# left is less
# right is more

@dataclass
class Node:
    key: Any = None
    value: Any = None
    left: Any = None
    right: Any = None


class Tree:
    key: Any = None
    value: Any = None
    left: Self = None
    right: Self = None 
    
    def addValue(self, n, key):
        if (self.key == key):
            self.value = value


