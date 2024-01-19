package alogrithms.graphs;

import java.util.ArrayList;
import java.util.List;

public class DirectedGraphString extends GraphString<String> {
    private List<List<EdgeString>> adjacencyListString;

    public DirectedGraphString(int vertices) {
        super(vertices);
        adjacencyListString = new ArrayList<>();
        for (int i = 0; i < vertices; i++) {
            adjacencyListString.add(new ArrayList<>());
        }
    }

    @Override
    public void addEdge(String v, String w, double weight) {
        super.addEdge(v, w, weight);
        adjacencyListString.get(verticesList.indexOf(v)).add(new EdgeString(v, w, weight));
    }

    @Override
    public void removeEdge(String v, String w) {
        super.removeEdge(v, w);
        adjacencyListString.get(verticesList.indexOf(v)).removeIf(edge -> edge.v2.equals(w));
    }

    @Override
    public int degree(String v) {
        return adjacencyListString.get(verticesList.indexOf(v)).size();
    }

    @Override
    public Iterable<String> vertices() {
        return verticesList;
    }

    @Override
    public Iterable<EdgeString> edges() {
        List<EdgeString> edgesList = new ArrayList<>();
        for (int v = 0; v < verticesList.size(); v++) {
            edgesList.addAll(adjacencyListString.get(v));
        }
        return edgesList;
    }

    @Override
    public Iterable<EdgeString> adjacent(String v) {
        return adjacencyListString.get(verticesList.indexOf(v));
    }

    // * Uppgift 5

    public static Iterable<String> breadthFirstSearch(DirectedGraphString graph, String startVertex) {
        List<String> traversalOrder = new ArrayList<>();
        boolean[] visited = new boolean[graph.getVertices()];

        int startIndex = graph.verticesList.indexOf(startVertex);
        if (startIndex != -1) {
            breadthFirstSearchUtil(graph, startIndex, visited, traversalOrder);
        }

        return traversalOrder;
    }

    private static void breadthFirstSearchUtil(DirectedGraphString graph, int start, boolean[] visited,
            List<String> traversalOrder) {
        int[] queue = new int[graph.getVertices()];
        int front = 0, rear = -1;

        visited[start] = true;
        queue[++rear] = start;

        while (front <= rear) {
            int currentVertex = queue[front++];
            traversalOrder.add(graph.verticesList.get(currentVertex));

            for (EdgeString edge : graph.adjacent(graph.verticesList.get(currentVertex))) {
                int index = graph.verticesList.indexOf(edge.v2);
                if (!visited[index]) {
                    visited[index] = true;
                    queue[++rear] = index;
                }
            }
        }
    }

}
