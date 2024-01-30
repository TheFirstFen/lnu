package alogrithms.graphs;

import java.util.List;

import alogrithms.Heap;

import java.util.ArrayList;
import java.util.Arrays;

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

    public void dfs(T startVertex) {
        boolean[] visited = new boolean[vertices];
        dfsRec(startVertex, visited, "dfs");
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

    public void bfs(int startVertex) {
        boolean[] visited = new boolean[vertices];

        int[] q = new int[vertices];
        int front = 0, rear = 0;

        visited[startVertex] = true;
        q[rear++] = startVertex;

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

    private boolean dfsPath(T vertex, T dest, boolean[] visited, List<T> path) {
        visited[(int) vertex] = true;
        path.add(vertex);

        if (vertex == dest) {
            return true;
        }

        for (Edge<T> edge : adjacencyList.get((int) vertex)) {
            int n = (int) edge.v2;
            if (!visited[n] && dfsPath(edge.v2, dest, visited, path)) {
                return true;
            }
        }

        path.remove(path.size() - 1);
        return false;
    }

    // * Uppgift 4
    public double[] dijkstra(int src) {
        double[] dist = new double[vertices];
        Arrays.fill(dist, Double.POSITIVE_INFINITY);
        dist[src] = 0;

        Heap<T> minHeap = new Heap<T>(vertices);
        for (int i = 0; i < vertices; i++) {
            minHeap.insert(new Edge(src, i, dist[i]));
        }

        while (!minHeap.isEmpty()) {
            Edge<T> minEdge = minHeap.poll();
            int u = (int) minEdge.v2;

            for (Edge<T> neighbor : adjacent(minEdge.v2)) {
                int v = (int) neighbor.v2;
                double weight = neighbor.weight;

                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    minHeap.insert(new Edge<T>(minEdge.v2, neighbor.v2, dist[v]));
                }
            }
        }

        return dist;
    }

    public double[] bellmanFord(int src) {
        double[] dist = new double[vertices];
        Arrays.fill(dist, Double.POSITIVE_INFINITY);
        dist[src] = 0;

        for (int i = 1; i < vertices - 1; i++) {
            for (Edge<T> edge : edges()) {
                int u = (int) edge.v1;
                int v = (int) edge.v2;
                double weight = edge.weight;

                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                }
            }
        }

        return dist;
    }
}