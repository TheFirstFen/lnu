import random
from BstSet import BstSet


def generate_lst(height):
    size = (2**height) - 1
    elements = []
    max_elements = 10_000
    while size > 0:
        element = random.randint(1, max_elements)
        while element in elements:
            element = random.randint(1, max_elements)
        elements.append(element)
        size -= 1
    return elements


height = 10     # gives exactly 1023 elements
lst = generate_lst(height)
bst = BstSet()

# before delete
for i in lst:
    bst.add(i)

with open("before_delete.txt", "w") as file:
    file.write(bst.pretty_dot())

# doing delete
for i in range(2000):
    values = []
    for j in range(512):
        value_to_delete = lst[random.randint(0, len(lst) - 1)]
        values.append(value_to_delete)
        bst.delete(value_to_delete)

    for k in range(len(values)):
        bst.add(values[k])

# after delete
with open("after_delete.txt", "w") as file:
    file.write(bst.pretty_dot())
