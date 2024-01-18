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
        // List<String> verticesList = new ArrayList<>(vertices);
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
    public static Iterable<String> topologicalSort(DirectedGraphString graph) {
        List<String> courseOrder = new ArrayList<>();
        boolean[] visited = new boolean[graph.getVertices()];

        for (String course : graph.vertices()) {
            int index = graph.verticesList.indexOf(course);
            if (!visited[index]) {
                topologicalSortUtil(graph, index, visited, courseOrder);
            }
        }

        return courseOrder;
    }

    private static void topologicalSortUtil(DirectedGraphString graph, int v, boolean[] visited,
            List<String> courseOrder) {
        visited[v] = true;

        for (EdgeString edge : graph.adjacent(graph.verticesList.get(v))) {
            int index = graph.verticesList.indexOf(edge.v2);
            if (!visited[index]) {
                topologicalSortUtil(graph, index, visited, courseOrder);
            }
        }

        courseOrder.add(graph.verticesList.get(v));
    }
}
