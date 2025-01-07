import random
import matplotlib.pyplot as plt
from BstSet import BstSet
import math


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
mean_max_depths = []
runs = 10

for h in range(min_height, max_height+1):
    max_depths = []
    for i in range(runs):
        bst = BstSet()
        lst = generate_lst(h)
        for j in lst:
            bst.add(j)

        max_depths.append(bst.max_depth())
    mean_max_depths.append(sum(max_depths) / len(max_depths))


plt.plot(sizes, mean_max_depths, "*", label="BST")
plt.plot(sizes, complete_depth, ">", label="Complete")
plt.legend()
plt.xlabel("Tree Sizes")
plt.ylabel("Depth")
plt.title("Depth of Random Input Trees")
plt.show()

log2_tree_sizes = [math.log2(i) for i in sizes]

plt.plot(log2_tree_sizes, mean_max_depths, "*", label="BST")
plt.plot(log2_tree_sizes, complete_depth, ">", label="Complete depth")

plt.legend()
plt.xlabel("Log of Tree sizes")
plt.ylabel("Max Depths (average 10 runs)")
plt.title("Depth of Random Input Trees")
plt.show()
