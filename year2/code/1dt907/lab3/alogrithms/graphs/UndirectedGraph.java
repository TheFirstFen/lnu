package alogrithms.graphs;

import java.util.*;

public class UndirectedGraph extends IGraph {
    private List<List<Integer>> adjacencyList;

    public UndirectedGraph(int vertices) {
        super(vertices);
        adjacencyList = new ArrayList<>();
        for (int i = 0; i < vertices; i++) {
            adjacencyList.add(new ArrayList<>());
        }
    }

    @Override
    public void addEdge(int v, int w) {
        super.addEdge(v, w);
        adjacencyList.get(v).add(w);
        adjacencyList.get(w).add(v);
    }

    @Override
    public void removeEdge(int v, int w) {
        super.removeEdge(v, w);
        adjacencyList.get(v).remove(Integer.valueOf(w));
        adjacencyList.get(w).remove(Integer.valueOf(v));
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
    public Iterable<Integer> edges() {
        List<Integer> edgesList = new ArrayList<>();
        for (int v = 0; v < vertices; v++) {
            for (int w : adjacencyList.get(v)) {
                if (v < w) {
                    edgesList.add(v);
                    edgesList.add(w);
                }
            }
        }
        return edgesList;
    }

    @Override
    public Iterable<Integer> adjacent(int v) {
        return adjacencyList.get(v);
    }
}