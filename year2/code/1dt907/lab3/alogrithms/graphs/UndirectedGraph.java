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

    public void dfs(int startVertex) {
        boolean[] visited = new boolean[vertices];
        dfsRec(startVertex, visited, "dfs");
    }

    private void dfsRec(int vertex, boolean[] visited, String callingFunc) {
        visited[vertex] = true;
        if (callingFunc.equals("dfs"))
            System.out.print(vertex + " ");

        for (Edge edge : adjacencyList.get(vertex)) {
            int n = edge.v2;
            if (!visited[n]) {
                dfsRec(n, visited, callingFunc);
            }
        }
    }

    public void bfs(int startVertex) {
        boolean[] visited = new boolean[vertices];

        int[] q = new int[vertices];
        int front = 0, rear = 0;

        visited[startVertex] = true;
        q[rear++] = startVertex;

        while (front != rear) {
            int curVertex = q[front++];
            System.out.print(curVertex + " ");

            for (Edge n : adjacencyList.get(curVertex)) {
                int nVertex = n.v2;
                if (!visited[nVertex]) {
                    visited[nVertex] = true;
                    q[rear++] = nVertex;
                }
            }
        }
    }

    @Override
    public boolean isConnected(int src, int dest) {
        boolean[] visited = new boolean[vertices];
        dfsRec(src, visited, "isConnected");
        return visited[dest];
    }

    @Override
    public Iterable<Integer> path(int src, int dest) {
        List<Integer> path = new ArrayList<>();
        boolean[] visited = new boolean[vertices];
        dfsPath(src, dest, visited, path);
        return path;
    }

    private boolean dfsPath(int vertex, int dest, boolean[] visited, List<Integer> path) {
        visited[vertex] = true;
        path.add(vertex);

        if (vertex == dest) {
            return true;
        }

        for (Edge edge : adjacencyList.get(vertex)) {
            int n = edge.v2;
            if (!visited[n] && dfsPath(n, dest, visited, path)) {
                return true;
            }
        }

        path.remove(path.size() - 1);
        return false;
    }
}