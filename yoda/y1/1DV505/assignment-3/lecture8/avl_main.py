import AvlSet as avl

avl = avl.AvlSet()
print("Adding 1 to 20 to the AVL tree")
for i in range(1, 21):
    avl.add(i)
print()
print(avl.dot())
print("search(10)", avl.search(10))
print("search(200)", avl.search(200))
print()
print("Deleting 1-10 from the AVL tree")
for i in range(1, 11):
    avl.delete(i)
print()
print(avl.dot())
