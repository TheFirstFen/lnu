from Graph import Graph
from Tree import Tree

# Create vertices for a graph
vertices = ["Seattle", "San Francisco", "Los Angeles",
            "Denver", "Kansas City", "Chicago", "Boston", "New York",
            "Atlanta", "Miami", "Dallas", "Houston"]

# Create an edge list for a graph
edges = [
    [0, 1], [0, 3], [0, 5],
    [1, 0], [1, 2], [1, 3],
    [2, 1], [2, 3], [2, 4], [2, 10],
    [3, 0], [3, 1], [3, 2], [3, 4], [3, 5],
    [4, 2], [4, 3], [4, 5], [4, 7], [4, 8], [4, 10],
    [5, 0], [5, 3], [5, 4], [5, 6], [5, 7],
    [6, 5], [6, 7],
    [7, 4], [7, 5], [7, 6], [7, 8],
    [8, 4], [8, 7], [8, 9], [8, 10], [8, 11],
    [9, 8], [9, 11],
    [10, 2], [10, 4], [10, 8], [10, 11],
    [11, 8], [11, 9], [11, 10]
]

# second test data
# 1. Friendship Network (Social Media Model): create a graph where vertices represent people, and edges represent friendships between them. 
# You can traverse the graph to find friends of friends, determine if there’s a connection between two people. The output is tested with "David" as starting node.
"""
vertices = ["Alice", "Bob", "Charlie", "David", "Emma", "Fiona", "George", "Helen"]
edges = [
    [0, 1], [0, 2], [1, 3], [1, 4],
    [2, 4], [3, 5], [4, 5], [5, 6], [6, 7]
]
"""

def print_search_result(graph, search_tree, traversal_type):
    searchOrders = search_tree.getSearchOrders()
    print(search_tree.getNumberOfVerticesFound(), 
          f"vertices are searched in this {traversal_type} order:")
    print(" ".join(graph.getVertex(i) for i in searchOrders))
    print()
    
    for i in range(len(searchOrders)):
        if search_tree.getParent(i) != -1:
            print(f"parent of {graph.getVertex(i)} is {graph.getVertex(search_tree.getParent(i))}")
    print()


graph = Graph(vertices, edges)  # Create a Graph

# Perform and print DFS result
dfs = graph.dfs(graph.getIndex("Chicago"))
print_search_result(graph, dfs, "DFS")
dfs.printTree()


# Perform and print BFS result
bfs = graph.bfs(graph.getIndex("Chicago"))
print_search_result(graph, bfs, "BFS")
bfs.printTree()

# second test data
# 1. Friendship Network (Social Media Model): create a graph where vertices represent people, and edges represent friendships between them. 
# You can traverse the graph to find friends of friends, determine if there’s a connection between two people. The output is tested with "David" as starting node.

vertices = ["Alice", "Bob", "Charlie", "David", "Emma", "Fiona", "George", "Helen"]
edges = [
    [0, 1], [0, 2], [1, 3], [1, 4],
    [2, 4], [3, 5], [4, 5], [5, 6], [6, 7]
]

graph = Graph(vertices, edges)  # Create a Graph

dfs = graph.dfs(graph.getIndex("David"))
print_search_result(graph, dfs, "DFS")
dfs.printTree()

# Perform and print BFS result
bfs = graph.bfs(graph.getIndex("David"))
print_search_result(graph, bfs, "BFS")
bfs.printTree()