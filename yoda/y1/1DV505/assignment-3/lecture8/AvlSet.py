# A BST based implementation of a set
# ==> no duplicate elements
# The implementation has two parts:
# - class BstSet   (Provided! No need to modify!)
# - class BstNode  (Not complete ==> add missing code)

class AvlNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.height = 1

    # finds the height of the node
    def get_height(self, node):
        return node.height if node else 0

    # finds the balance of the node
    def get_balance(self):
        return self.get_height(self.right) - self.get_height(self.left)

    # update height of the node
    def update_height(self):
        self.height = 1 + max(
            self.get_height(self.left),
            self.get_height(self.right)
        )

    # rotation to the left
    def rotate_left(self):
        # rotation
        new_root = self.right
        self.right = new_root.left
        new_root.left = self

        self.update_height()
        new_root.update_height()

        return new_root

    # rotation to the right
    def rotate_right(self):
        # rotation
        new_root = self.left
        self.left = new_root.right
        new_root.right = self

        self.update_height()
        new_root.update_height()

        return new_root

    # rebalancing the tree
    def rebalance(self):
        balance = self.get_balance()

        # right heavy
        if balance > 1:
            if self.right.get_balance() >= 0:   # RR rotation
                return self.rotate_left()
            else:
                self.right = self.right.rotate_right()  # RL rotation
                return self.rotate_left()

        # left heavy
        if balance < -1:
            if self.left.get_balance() <= 0:
                return self.rotate_right()  # LL rotation
            else:
                self.left = self.left.rotate_left()     # LR rotation
                return self.rotate_right()

        return self

    def add(self, val):
        if val < self.value:
            if self.left is None:
                self.left = AvlNode(val, None, None)
            else:
                self.left = self.left.add(val)
        elif val > self.value:
            if self.right is None:
                self.right = AvlNode(val, None, None)
            else:
                self.right = self.right.add(val)
        # update height and rebalance
        self.update_height()
        return self.rebalance()

    def __str__(self):
        txt = ""
        if self.left is not None:
            txt += self.left.__str__()
        txt += str(self.value) + " "
        if self.right is not None:
            txt += self.right.__str__()
        return txt

    def search(self, val):
        if not isinstance(val, (int, float)):
            raise ValueError("Search value has to be either a integer or"
                             " float value")

        if val == self.value:
            return True
        elif val < self.value:
            if self.left:
                return self.left.search(val)
            return False

        elif val > self.value:
            if self.right:
                return self.right.search(val)
            return False

        return False

    def count(self):
        counter = 1
        if self.right is not None:
            counter += self.right.count()
        if self.left is not None:
            counter += self.left.count()

        return counter

    def count_internal(self):
        counter = 0
        # makes sure it is not a leaf
        if self.left is not None or self.right is not None:
            counter += 1
            # if there is a leaf checks which one it is
            if self.right is not None:
                counter += self.right.count_internal()
            if self.left is not None:
                counter += self.left.count_internal()
        return counter

    def max_depth(self):
        # base case
        if self.value is None:
            return 0
        left_depth = right_depth = 0
        if self.left:
            left_depth = self.left.max_depth()

        if self.right:
            right_depth = self.right.max_depth()

        return 1 + max(left_depth, right_depth)

    def dot(self, parent):
        txt = ""
        if parent:
            txt += f"{parent}  --  {self.value}\n"

        balance = self.get_balance()

        txt += (
            f'{self.value} [label="{self.value} '
            f'({self.height}, {balance})"];\n'
        )

        if self.left:
            txt += self.left.dot(self.value)

        if self.right:
            txt += self.right.dot(self.value)

        return txt

    # Find node X to be deleted
    # - Case 1: X with no left child ==> replace X with right child of X
    # - Case 2: X as a left child ==> find max in left subtree,
    #           move max value to X and remove max node
    def delete(self, value, parent):
        if not isinstance(value, (int, float)):
            raise ValueError("Delete value has to be a float or an integer")

        if value < self.value:
            if self.left:
                return self.left.delete(value, self)
            return False
        elif value > self.value:
            if self.right:
                return self.right.delete(value, self)
            return False
        else:
            # no children
            if self.left is None and self.right is None:
                if parent:
                    if parent.left == self:
                        parent.left = None
                    elif parent.right == self:
                        parent.right = None
                return True
            # with only right child
            if self.left is None:
                if parent:
                    if parent.left == self:
                        parent.left = self.right
                    elif parent.right == self:
                        parent.right = self.right
                return True
            # with only left child
            elif self.right is None:
                if parent:
                    if parent.left == self:
                        parent.left = self.left
                    elif parent.right == self:
                        parent.right = self.left
                return True

            # with two children

            self.value = self.find_smallest_value(self.right)
            self.right = self.right.delete(self.value, self)
            self.update_height()
            return self.rebalance()


#
# The class BstSet
#
class AvlSet:

    def __init__(self):
        self.root = None

    # Adds value val to tree (if it doesn't already exist)
    def add(self, val):
        if self.root is None:
            self.root = AvlNode(val, None, None)
        else:
            self.root = self.root.add(val)

    # Returns a string representation of the tree values.
    # Sorted with smallest value first
    def __str__(self):
        txt = "{ "
        if self.root is not None:
            txt += self.root.__str__()
        return txt + "}"

    # Returns True if value val is stored in tree,
    # Otherwise False
    def search(self, val):
        if self.root is None:
            return False
        else:
            return self.root.search(val)

    # Count total number of nodes in the tree
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Count number of internal nodes
    # ==> not including leafs
    def count_internal(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_internal()

    # Number of nodes in longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Delete a node with value val from tree. Returns True if succesful
    # and False if value val doesn't exist in tree.
    # Extra care taken for removing the root.
    def delete(self, val):
        if self.root is None:  # Empty tree
            return False

        if self.root.value == val:  # Delete root
            if self.root.left is None:
                if self.root.right is None:  # Delete singleton
                    self.root = None
                    return True
                else:      # Case 1 for root
                    self.root = self.root.right  # Bypass root
        return self.root.delete(val, None)

    # Returns a string representing a DOT markup of
    # the BST suitable fror Graphvis Online.
    def dot(self):
        if self.root is None:
            return "No nodes ==> no graph markup"
        else:
            dot_text = "graph BST {\n"
            dot_text += self.root.dot(None)  # None as parent
            dot_text += "}"
            return dot_text
