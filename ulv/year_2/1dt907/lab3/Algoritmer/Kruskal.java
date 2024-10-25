package Algoritmer;

import java.util.List;
import java.util.ArrayList;

public class Kruskal {
    public static List<Graph.Edge> kruskal(Graph graph) {
        List<Graph.Edge> result = new ArrayList<>();

        Graph.Edge[] edges = getAllEdges(graph);
        HeapSort.heapSort(edges);

        WQUF unionFind = new WQUF(graph.getVertices());

        for (Graph.Edge edge : edges) {
            int start = edge.start;
            int end = edge.end;

            if (!unionFind.Connected(start, end)) {
                result.add(edge);
                unionFind.union(start, end);
            }
        }
        return result;
    }

    private static Graph.Edge[] getAllEdges(Graph graph) {
        List<Graph.Edge> alledges = new ArrayList<>();

        for (Iterable<Graph.Edge> edges : graph.adj) {
            for (Graph.Edge edge : edges) {
                alledges.add(edge);
            }
        }
        return alledges.toArray(new Graph.Edge[0]);
    }

    public static List<List<Graph.Edge>> groupEdgesByConnectedComponents(List<Graph.Edge> edges, int numVertices) {
        List<List<Graph.Edge>> connectedComponents = new ArrayList<>();
        WQUF uf = new WQUF(numVertices);
    
        for (Graph.Edge edge : edges) {
            int start = edge.start;
            int end = edge.end;
    
            if (!uf.Connected(start, end)) {
                uf.union(start, end);
            }
        }
    
        @SuppressWarnings("unchecked")
        List<Integer>[] componentVerticesArray = new List[numVertices];
        for (int i = 0; i < numVertices; i++) {
            int root = uf.find(i);
            if (componentVerticesArray[root] == null) {
                componentVerticesArray[root] = new ArrayList<>();
            }
            componentVerticesArray[root].add(i);
        }
    
        for (List<Integer> componentVertices : componentVerticesArray) {
            if (componentVertices != null && !componentVertices.isEmpty()) {
                List<Graph.Edge> componentEdges = new ArrayList<>();
                for (Graph.Edge edge : edges) {
                    if (componentVertices.contains(edge.start) && componentVertices.contains(edge.end)) {
                        componentEdges.add(edge);
                    }
                }
                connectedComponents.add(componentEdges);
            }
        }
        return connectedComponents;
    }

    public static void main(String[] args) {
        UndirectedGraph graph = new UndirectedGraph(5);
        graph.addEdge(0, 1, 2.0);
        graph.addEdge(0, 2, 1.5);
        graph.addEdge(1, 2, 3.0);
        graph.addEdge(2, 3, 1.2);
        graph.addEdge(3, 4, 4.0);

        List<Graph.Edge> minimumSpanningTree = kruskal(graph);

        System.out.println("Minimum Spanning Tree Edges:");
        for (Graph.Edge edge : minimumSpanningTree) {
            System.out.println(edge);
        }
    }
}