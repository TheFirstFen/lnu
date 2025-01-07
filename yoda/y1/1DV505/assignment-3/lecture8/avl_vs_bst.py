import math
import matplotlib.pyplot as plt
import random
from AvlSet import AvlSet

import sys
sys.path.append("../lecture7")
from BstSet import BstSet


avl = AvlSet()
bst = BstSet()


def generate_lst(height):
    size = (2**height) - 1
    elements = set()
    max_element = size**2
    while len(elements) < size:
        element = random.randint(1, max_element)
        elements.add(element)
    return list(elements)


min_height = 5
max_height = 20
sizes = [(2**h)-1 for h in range(min_height, max_height+1)]
complete_depth = [(math.log2(size+1))-1 for size in sizes]
mean_max_depths_bst = []
mean_max_depths_avl = []
runs = 10


for h in range(min_height, max_height+1):
    max_depths_bst = []
    max_depths_avl = []
    for i in range(runs):
        bst = BstSet()
        avl = AvlSet()
        lst = generate_lst(h)
        for j in lst:
            bst.add(j)
            avl.add(j)

        max_depths_bst.append(bst.max_depth())
        max_depths_avl.append(avl.max_depth())
    mean_max_depths_bst.append(sum(max_depths_bst) / len(max_depths_bst))
    mean_max_depths_avl.append(sum(max_depths_avl) / len(max_depths_avl))


plt.plot(sizes, mean_max_depths_bst, "*", label="BST")
plt.plot(sizes, mean_max_depths_avl, "+", label="AVL")
plt.plot(sizes, complete_depth, ">", label="Complete")
plt.legend()
plt.xlabel("Tree Sizes")
plt.ylabel("Depth")
plt.title("Depth of Random Input Trees")
plt.show()

log2_tree_sizes = [math.log2(i) for i in sizes]

plt.plot(log2_tree_sizes, mean_max_depths_bst, "*", label="BST")
plt.plot(log2_tree_sizes, mean_max_depths_avl, "+", label="AVL")
plt.plot(log2_tree_sizes, complete_depth, ">", label="Complete")

plt.legend()
plt.xlabel("Log of Tree sizes")
plt.ylabel("Max Depths (average 10 runs)")
plt.title("Depth of Random Input Trees")
plt.show()
