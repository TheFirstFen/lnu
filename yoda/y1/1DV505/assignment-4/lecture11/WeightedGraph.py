from misc.Graph import Graph
from WeightedEdge import WeightedEdge
from misc.Tree import Tree


class WeightedGraph(Graph):
    def __init__(self, vertices=[], edges=[]):
        super().__init__(vertices, edges)

    # Pseudocode for Adjacency List method (You need to write the code)
    def getAdjacencyLists(self, edges):

        self.neighbors = [[] for i in range(len(self.vertices))]

        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            w = edges[i][2]
            self.neighbors[u].append(WeightedEdge(u, v, w))

        return self.neighbors

    # Display edges with weights
    def printWeightedEdges(self):
        for i in range(len(self.neighbors)):
            for edge in self.neighbors[i]:
                print(str(self.getVertex(edge.v)) + ", " + str(edge.weight))
            print()

    # Return the weight between two vertices
    def getWeight(self, u, v):
        for edge in self.neighbors[self.getIndex(u)]:
            if edge.v == v:
                return edge.w
        return None

    # Override the addEdge method to add a weighted edge
    def addEdge(self, u, v, w):
        self.neighbors[u].append(WeightedEdge(u, v, w))

    # Get a minimum spanning tree rooted at the specified vertex
    def getMinimumSpanningTree(self, startingVertex=0):
        T = list()
        cost = self.getSize() * [float('inf')]
        cost[startingVertex] = 0
        parent = self.getSize() * [-1]
        total_weight = 0

        while len(T) < self.getSize():
            min_cost = float('inf')
            u = -1
            for v in range(self.getSize()):
                if v not in T and cost[v] < min_cost:
                    min_cost = cost[v]
                    u = v
            if u == -1:
                break
            else:
                T.append(u)
            total_weight += min_cost

            for n in self.neighbors[u]:
                if n.v not in T and cost[n.v] > n.weight:
                    cost[n.v] = n.weight
                    parent[n.v] = u

        return MST(startingVertex, parent, T, total_weight, self.vertices)

    # Find single source shortest paths
    def getShortestPath(self, sourceVertex):
        T = list()
        cost = self.getSize() * [float('inf')]
        cost[sourceVertex] = 0
        parent = self.getSize() * [-1]

        while len(T) < self.getSize():
            min_cost = float('inf')
            u = -1
            for v in range(self.getSize()):
                if v not in T and cost[v] < min_cost:
                    min_cost = cost[v]
                    u = v
            if u == -1:
                break
            else:
                T.append(u)

            for edge in self.neighbors[u]:
                if edge.v not in T and cost[u] + edge.weight < cost[edge.v]:
                    cost[edge.v] = cost[u] + edge.weight
                    parent[edge.v] = u

        return ShortestPathTree(sourceVertex, parent, list(T), cost,
                                self.vertices)


# MST is a subclass of Tree which you have implemented it in the preceding assignment
class MST(Tree):
    def __init__(self, startingIndex, parent, T, totalWeight, vertices):
        super().__init__(startingIndex, parent, T, vertices)
        self.totalWeight = totalWeight

    def getTotalWeight(self):
        return self.totalWeight

    def dot(self):
        dot = "graph MST {\n"
        for i in range(len(self.vertices)):
            dot += "\t" + str(self.vertices[i]) + ";\n"
        for i in range(len(self.vertices)):
            if self.parent[i] != -1:
                dot += f"\t{self.vertices[self.parent[i]]} -- "
                + f"{self.vertices[i]};\n"
        dot += f"\tlabel = \"Total Weight: {self.totalWeight}\";\n"
        dot += "}"
        return dot


class ShortestPathTree(Tree):
    def __init__(self, sourceIndex, parent, T, costs, vertices):
        super().__init__(sourceIndex, parent, T, vertices)
        self.costs = costs

    # Return the cost for a path from the root to vertex v
    def getCost(self, v):
        return self.costs[v]

    # Print paths from all vertices to the source
    def printAllPaths(self):
        for i in range(len(self.costs)):
            self.printPath(i)
            print("Cost:", self.costs[i])

    def dot(self):
        dot = "graph SPT {\n"
        for i in range(len(self.vertices)):
            dot += "\t" + str(self.vertices[i]) + ";\n"
        total_cost = 0
        for i in range(len(self.vertices)):
            if self.parent[i] != -1:
                weight = self.costs[i] - self.costs[self.parent[i]]
                dot += f"\t{self.vertices[self.parent[i]]} -- "
                + f"{self.vertices[i]} [label={weight}];\n"
                total_cost += weight
        dot += f"\tlabel = \"Total Cost: {total_cost}\";\n"
        dot += "}"
        return dot
