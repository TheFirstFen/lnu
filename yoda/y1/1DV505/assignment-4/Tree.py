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
        pass

    # Print a path from the root to vertex v
    def printPath(self, index):
        pass

    # Print the whole tree
    def printTree(self):
        pass
