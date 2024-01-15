package alogrithms.graphs;

import java.util.List;
import java.util.ArrayList;

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

    @Override
    public boolean isConnected(int source, int destination) {
        boolean[] visited = new boolean[vertices];
        dfs(source, visited);
        return visited[destination];
    }

    private void dfs(int vertex, boolean[] visited) {
        visited[vertex] = true;
        for (Edge edge : adjacencyList.get(vertex)) {
            if (!visited[edge.v2]) {
                dfs(edge.v2, visited);
            }
        }
    }

    @Override
    public Iterable<Integer> path(int source, int destination) {
        List<Integer> path = new ArrayList<>();
        boolean[] visited = new boolean[vertices];
        dfsWithPath(source, destination, visited, path);
        return path;
    }

    private boolean dfsWithPath(int current, int destination, boolean[] visited, List<Integer> path) {
        visited[current] = true;
        path.add(current);

        if (current == destination) {
            return true;
        }

        for (Edge edge : adjacencyList.get(current)) {
            if (!visited[edge.v2]) {
                if (dfsWithPath(edge.v2, destination, visited, path)) {
                    return true;
                }
            }
        }

        path.remove(path.size() - 1);
        return false;
    }
}