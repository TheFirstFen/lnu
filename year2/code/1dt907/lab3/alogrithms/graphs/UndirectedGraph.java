package alogrithms.graphs;

import java.util.List;
import java.util.ArrayList;

public class UndirectedGraph<T> extends Graph<T> {
    private List<List<Edge<T>>> adjacencyList;

    public UndirectedGraph(int vertices) {
        super(vertices);
        adjacencyList = new ArrayList<>();
        for (int i = 0; i < vertices; i++) {
            adjacencyList.add(new ArrayList<>());
        }
    }

    @Override
    public void addEdge(T v, T w, double weight) {
        super.addEdge(v, w, weight);
        adjacencyList.get((int) v).add(new Edge<T>(v, w, weight));
        adjacencyList.get((int) w).add(new Edge<T>(w, v, weight));
    }

    @Override
    public void removeEdge(T v, T w) {
        super.removeEdge(v, w);
        adjacencyList.get((int) v).removeIf(edge -> edge.v2 == w);
        adjacencyList.get((int) w).removeIf(edge -> edge.v2 == v);
    }

    @Override
    public int degree(T v) {
        return adjacencyList.get((int) v).size();
    }

    @Override
    public Iterable<T> vertices() {
        return verticesList;
    }

    @Override
    public Iterable<Edge<T>> edges() {
        List<Edge<T>> edgesList = new ArrayList<>();
        for (int v = 0; v < vertices; v++) {
            for (Edge<T> edge : adjacencyList.get(v)) {
                if (v < (int) edge.v2) {
                    edgesList.add(new Edge<T>(edge.v1, edge.v2, edge.weight));
                }
            }
        }
        return edgesList;
    }

    @Override
    public Iterable<Edge<T>> adjacent(T v) {
        return adjacencyList.get((int) v);
    }

    public void dfs(T start) {
        boolean[] visited = new boolean[vertices];
        dfsRec(start, visited, "dfs");
    }

    private void dfsRec(T src, boolean[] visited, String callingFunc) {
        visited[(int) src] = true;
        if (callingFunc.equals("dfs"))
            System.out.print(src + " ");

        for (Edge<T> edge : adjacencyList.get((int) src)) {
            int n = (int) edge.v2;
            if (!visited[n]) {
                dfsRec(edge.v2, visited, callingFunc);
            }
        }
    }

    public void bfs(int start) {
        boolean[] visited = new boolean[vertices];

        int[] q = new int[vertices];
        int front = 0, rear = 0;

        visited[start] = true;
        q[rear++] = start;

        while (front != rear) {
            int curVertex = q[front++];
            System.out.print(curVertex + " ");

            for (Edge<T> n : adjacencyList.get(curVertex)) {
                int nVertex = (int) n.v2;
                if (!visited[nVertex]) {
                    visited[nVertex] = true;
                    q[rear++] = nVertex;
                }
            }
        }
    }

    @Override
    public boolean isConnected(T src, T dest) {
        boolean[] visited = new boolean[vertices];
        dfsRec(src, visited, "isConnected");
        return visited[(int) dest];
    }

    @Override
    public Iterable<T> path(T src, T dest) {
        List<T> path = new ArrayList<>();
        boolean[] visited = new boolean[vertices];
        dfsPath(src, dest, visited, path);
        return path;
    }

    private boolean dfsPath(T v, T dest, boolean[] visited, List<T> path) {
        visited[(int) v] = true;
        path.add(v);

        if (v == dest) {
            return true;
        }

        for (Edge<T> edge : adjacencyList.get((int) v)) {
            int n = (int) edge.v2;
            if (!visited[n] && dfsPath(edge.v2, dest, visited, path)) {
                return true;
            }
        }

        path.remove(path.size() - 1);
        return false;
    }
}