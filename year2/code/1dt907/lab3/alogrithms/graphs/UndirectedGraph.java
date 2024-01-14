package alogrithms.graphs;

import java.util.*;

public class UndirectedGraph extends Graph {
    private List<List<Edge>> adjacencyList;

    public UndirectedGraph(int vertices) {
        super(vertices);
        adjacencyList = new ArrayList<>();
        for (int i = 0; i < vertices; i++) {
            adjacencyList.add(new ArrayList<>());
        }
    }

    @Override
    public void addEdge(int v, int w, double weight) {
        super.addEdge(v, w, weight);
        adjacencyList.get(v).add(new Edge(v, w, weight));
        adjacencyList.get(w).add(new Edge(w, v, weight));
    }

    @Override
    public void removeEdge(int v, int w) {
        super.removeEdge(v, w);
        adjacencyList.get(v).removeIf(edge -> edge.v2 == w);
        adjacencyList.get(w).removeIf(edge -> edge.v2 == v);
    }

    @Override
    public int degree(int v) {
        return adjacencyList.get(v).size();
    }

    @Override
    public Iterable<Integer> vertices() {
        List<Integer> verticesList = new ArrayList<>();
        for (int i = 0; i < vertices; i++) {
            verticesList.add(i);
        }
        return verticesList;
    }

    @Override
    public Iterable<Edge> edges() {
        List<Edge> edgesList = new ArrayList<>();
        for (int v = 0; v < vertices; v++) {
            for (Edge edge : adjacencyList.get(v)) {
                if (v < edge.v2) {
                    edgesList.add(new Edge(v, edge.v2, edge.weight));
                }
            }
        }
        return edgesList;
    }

    @Override
    public Iterable<Edge> adjacent(int v) {
        return adjacencyList.get(v);
    }
}