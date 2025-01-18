
from .Tree import Tree
from .Queue import Queue


class Graph:
    def __init__(self, vertices = [], edges = []):
        self.vertices = vertices
        self.neighbors = self.getAdjacencyLists(edges)

    # Return a list of adjacency lists for edges
    def getAdjacencyLists(self, edges):
        neighbors = []
        for i in range(len(self.vertices)):
            neighbors.append([])  # Each element is another list

        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            neighbors[u].append(Edge(u, v))  # Insert an edge (u, v)

        return neighbors

    # Return the number of vertices in the graph
    def getSize(self):
        return len(self.vertices)

    # Return the vertices in the graph
    def getVertices(self):
        return self.vertices

    # Return the vertex at the specified index
    def getVertex(self, index):
        return self.vertices[index]

    # Return the index for the specified vertex
    def getIndex(self, v):
        return self.vertices.index(v)

    # Return the neighbors of vertex with the specified index
    def getNeighbors(self, index):
        return self.neighbors[index]

    # Return the degree for a specified vertex
    def getDegree(self, v):
        pass

    # Print the edges
    def printEdges(self):
        for u in range(0, len(self.neighbors)):
            print(str(self.getVertex(u)) + " (" + str(u) + "): ", end = "")
            for j in range(len(self.neighbors[u])):
                print("(" + str(u) + ", " +
                      str(self.neighbors[u][j].v), end = ") ")
            print()

    # Clear graph
    def clear(self):
        self.vertices = []
        self.neighbors = []
     
    def addVertex(self, vertex):
       if not(vertex in self.vertices):
           self.vertices.append(vertex)
           self.neighbors.append([]) 
   
    def addEdge(self, u, v):
        if u in self.vertices and v in self.vertices:
            indexU = self.getIndex(u)
            indexV = self.getIndex(v)
            self.neighbors[indexU].append(Edge(indexU, indexV))



# Obtain a DFS tree starting from vertex v
    def dfs(self, v):
        searchOrders = []
        parent = len(self.vertices) * [-1]  # Initialize parent[i] to -1

        # Mark visited vertices
        isVisited = len(self.vertices) * [False]

        # Recursively search
        self.dfsHelper(v, parent, searchOrders, isVisited)

        # Return a search tree
        return Tree(v, parent, searchOrders, self.vertices)

# Recursive method for DFS search
    def dfsHelper(self, v, parent, searchOrders, isVisited):
        # Store the visited vertex
        searchOrders.append(v)
        isVisited[v] = True  # Vertex v visited

        for e in self.neighbors[v]:
            w = e.v  # e.v is w in Listing 22.6
            if not isVisited[w]:
                parent[w] = v  # The parent of vertex w is v
                # Recursive search
                self.dfsHelper(w, parent, searchOrders, isVisited)


# Starting bfs search from vertex v
    def bfs(self, v):
        searchOrders = []
        parent = len(self.vertices) * [-1]  # Initialize parent[i] to -1

        queue = Queue()  # The Queue class is defined in Chapter 18
        isVisited = len(self.vertices) * [False]
        queue.enqueue(v)  # Enqueue v
        isVisited[v] = True  # Mark it visited

        while not queue.isEmpty():
            u = queue.dequeue()  # Dequeue to u
            searchOrders.append(u)  # u searched
            for e in self.neighbors[u]:
                w = e.v  # e.v is w in Listing 22.9
                if not isVisited[w]:
                    queue.enqueue(w)  # Enqueue w
                    parent[w] = u  # The parent of vertex w is u
                    isVisited[w] = True #Mark it visited
        return Tree(v, parent, searchOrders, self.vertices)


        
class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v