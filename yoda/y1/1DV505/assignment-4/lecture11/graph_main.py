from WeightedGraph import WeightedGraph


def read_adjacency_list(file_path):
    adjacency_list = {}
    with open(file_path, "r") as file:
        for line in file:
            animal_info = line.split()
            key = animal_info[0].replace(":", "")
            animal_info.pop(0)
            adjacency_list[key] = list()

            for i in range(0, len(animal_info), 2):
                animal = animal_info[i]
                freq = int(animal_info[i+1].replace(",", ""))
                adjacency_list[key].append((animal, freq))

        return adjacency_list


def extract_vertices_and_edges(adjacency_list):
    vertices = []
    edges = []
    for v in adjacency_list.keys():
        vertices.append(v)
    for key in adjacency_list:
        key_idx = vertices.index(key)
        for j in adjacency_list[key]:
            animal = j[0]
            weight = j[1]
            animal_idx = vertices.index(animal)
            edges.append([key_idx, animal_idx, weight])
    return vertices, edges


# Assuming the file path is 'graph.txt'
adjacency_list = read_adjacency_list('graph.txt')
vertices, edges = extract_vertices_and_edges(adjacency_list)

graph = WeightedGraph(vertices, edges)

mst = graph.getMinimumSpanningTree(graph.getIndex("Lion"))
print("Minimum Spanning Tree")
print(mst.dot())
print()
print("Djikstra's Shortest Path")
spt = graph.getShortestPath(graph.getIndex("Lion"))
print(spt.dot())

print(spt.printAllPaths())
