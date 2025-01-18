class Tree:
    def __init__(self, root, parent, searchOrders, vertices):
        self.root = root
        self.parent = parent
        self.searchOrders = searchOrders
        self.vertices = vertices

    # Return the root of the tree
    def getRoot(self):
        return self.root

    # Return the parent of vertex v
    def getParent(self, index):
        return self.parent[index]

    # Return an array representing search order
    def getSearchOrders(self):
        return self.searchOrders

    # Return number of vertices found
    def getNumberOfVerticesFound(self):
        return len(self.searchOrders)

    # Return the path of vertices from a vertex index to the root
    def getPath(self, index):
        path = []
        while index != -1:
            path.append(self.vertices[index])
            index = self.parent[index]
        return path[::-1]

    # Print a path from the root to vertex v
    def printPath(self, index):
        print(f"Path from {self.vertices[self.root]}"
              f" to {self.vertices[index]}: ",  end="")
        path = self.getPath(index)
        for i in path:
            if i != path[-1]:
                print(i, end=" -> ")
            else:
                print(i)
        print()

    # Print the whole tree
    def printTree(self):
        print(f"Root is: {self.vertices[self.root]}")
        for i in range(len(self.vertices)):
            if self.parent[i] != -1:
                print(f"parent of {self.vertices[i]} is "
                      f"{self.vertices[self.parent[i]]}")
            else:
                print(f"parent of {self.vertices[i]} is None")
        print()
