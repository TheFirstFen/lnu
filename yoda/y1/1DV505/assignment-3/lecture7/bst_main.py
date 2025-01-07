import BstSet as bst

data = [23, 12, 37, 6, 15, 14, 7, 30, 32, 29, 29]

print("\nProvided")
bst = bst.BstSet()
for n in data:
    bst.add(n)
print("__str__", bst)

print("\nMandatory")
print("search(30)", bst.search(30))
print("search(31)", bst.search(31))

print("size", bst.size())
print("count_internal", bst.count_internal())
print("max_depth", bst.max_depth())

print("lr_inorder", bst.lr_inorder())
print("rl_postorder", bst.rl_postorder())

print("dot printout")
print(bst.dot())
print("\ndelete(6)", bst.delete(6))
print("delete(8)", bst.delete(8))
print("delete(37)", bst.delete(37))
print("delete(23)", bst.delete(23))
print("size", bst.size())
print("max_depth", bst.max_depth())
print("dot printout after delete")
print(bst.dot())

print("\nVG Exercises")
print("max_depth", bst.max_depth())
print("pretty dot printout")
print(bst.pretty_dot())
