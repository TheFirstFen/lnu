from Tree import Tree
from Queue import Queue


class Graph:
    def __init__(self, vertices=[], edges=[]):
        self.vertices = vertices
        self.neighbors = self.getAdjacencyLists(edges)

    # Return a list of adjacency lists for edges
    def getAdjacencyLists(self, edges):
        neighbors = []
        for v in range(len(self.vertices)):
            neighbors.append([])

        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            neighbors[u].append(Edge(v, u))
        return neighbors

    # Return the number of vertices in the graph
    def getSize(self):
        return len(self.vertices)

    # Return the vertices in the graph
    def getVertices(self):
        return self.vertices

    # Return the vertex at the specified index
    def getVertex(self, index):
        if 0 <= index < len(self.vertices):
            return self.vertices[index]
        return None

    # Return the index for the specified vertex
    def getIndex(self, v):
        return self.vertices.index(v)

    # Return the neighbors of vertex with the specified index
    def getNeighbors(self, index):
        v = self.getVertex(index)
        idx = self.getIndex(v)
        return [edge.u for edge in self.neighbors[idx]]

    # Return the degree for a specified vertex
    def getDegree(self, v):
        return len(self.neighbors[self.getIndex(v)])

    # Print the edges
    def printEdges(self):
        for u in range(len(self.neighbors)):
            print(f"Vertex {self.vertices[u]}: ", end="")
            for edge in self.neighbors[u]:
                print(f"({self.vertices[edge.u]}, {self.vertices[edge.v]})",
                      end=" ")
            print()

    # Clear graph
    def clear(self):
        self.vertices = []
        self.neighbors = []

    def addVertex(self, vertex):
        self.vertices.append(vertex)

    def addEdge(self, u, v):
        self.neighbors[u].append(Edge(u, v))

    # Obtain a DFS tree starting from vertex v
    def dfs(self, v):
        parent = [-1] * len(self.vertices)
        isVisited = [False] * len(self.vertices)
        isVisited[v] = True
        searchOrders = []

        self.dfsHelper(v, parent, searchOrders, isVisited)
        return Tree(v, parent, searchOrders, self.vertices)

    # Recursive method for DFS search
    def dfsHelper(self, v, parent, searchOrders, isVisited):
        searchOrders.append(v)

        for w in self.getNeighbors(v):
            if not isVisited[w]:
                parent[w] = v
                isVisited[w] = True
                self.dfsHelper(w, parent, searchOrders, isVisited)

    # Starting bfs search from vertex v
    def bfs(self, v):
        queue = Queue()
        queue.enqueue(v)

        isVisited = [False] * len(self.vertices)
        isVisited[v] = True

        parent = [-1] * len(self.vertices)
        traversed_vertices = []

        while not queue.isEmpty():
            u = queue.dequeue()
            traversed_vertices.append(u)

            for w in self.getNeighbors(u):
                if not isVisited[w]:
                    queue.enqueue(w)
                    isVisited[w] = True
                    parent[w] = u
        return Tree(v, parent, traversed_vertices, self.vertices)


class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v
