from BST import BinaryTree, Node
import random
import sys

tree = BinaryTree()

amount = int(sys.argv[1])
max_limit = 30

for i in range(1, amount+1):
    # n = random.randint(1, max_limit)
    tree.insert(Node(i))

# n = int(sys.argv[2]) # random.randint(1, max_limit)
# print("Searching for:", n)
for n in range(1, amount+1):
    try:
        if n != 1:
            assert tree.findNode(Node(n)) is None, "Should not be none"
    except AssertionError as e:
        print(n, e)
        
# Print the tree
# print(tree.root)
# tree.printTree()  # This should print the values in sorted order

