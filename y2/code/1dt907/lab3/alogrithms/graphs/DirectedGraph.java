package alogrithms.graphs;

import alogrithms.HeapDirected;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class DirectedGraph<T> extends GraphDirected<T> {
    private List<List<EdgeDirected<T>>> adjacencyList;

    public DirectedGraph(int vertices) {
        super(vertices);
        adjacencyList = new ArrayList<>();
        for (int i = 0; i < vertices; i++) {
            adjacencyList.add(new ArrayList<>());
        }
    }

    @Override
    public void addEdge(T v, T w, double weight) {
        super.addEdge(v, w, weight);
        adjacencyList.get(verticesList.indexOf(v)).add(new EdgeDirected<T>(v, w, weight));
    }

    @Override
    public void removeEdge(T v, T w) {
        super.removeEdge(v, w);
        adjacencyList.get(verticesList.indexOf(v)).removeIf(edge -> edge.v2 == w);
    }

    @Override
    public int degree(T v) {
        return adjacencyList.get(verticesList.indexOf(v)).size();
    }

    public List<T> verticesList() {
        return verticesList;
    }

    @Override
    public Iterable<T> vertices() {
        return verticesList;
    }

    @Override
    public Iterable<EdgeDirected<T>> edges() {
        List<EdgeDirected<T>> edgesList = new ArrayList<>();
        for (int v = 0; v < vertices; v++) {
            edgesList.addAll(adjacencyList.get(v));
        }
        return edgesList;
    }

    @Override
    public Iterable<EdgeDirected<T>> adjacent(T v) {
        return adjacencyList.get((int) v);
    }

    public Iterable<EdgeDirected<T>> adjacent(int v) {
        return adjacencyList.get(v);
    }

    // * Uppgift 2
    public void dfs(T start) {
        boolean[] visited = new boolean[vertices];
        dfsRec(start, visited, "dfs");
    }

    private void dfsRec(T v, boolean[] visited, String callingFunc) {
        visited[(int) v] = true;
        if (callingFunc.equals("dfs"))
            System.out.print(v + " ");

        for (EdgeDirected<T> edge : adjacencyList.get((int) v)) {
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

            for (EdgeDirected<T> n : adjacencyList.get(curVertex)) {
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

        for (EdgeDirected<T> edge : adjacencyList.get((int) v)) {
            int n = (int) edge.v2;
            if (!visited[n] && dfsPath(edge.v2, dest, visited, path)) {
                return true;
            }
        }

        path.remove(path.size() - 1);
        return false;
    }

    // * Uppgift 4
    @SuppressWarnings({ "unchecked", "rawtypes" })
    public double[] dijkstra(int src) {
        double[] dist = new double[vertices];
        Arrays.fill(dist, Double.POSITIVE_INFINITY);
        dist[src] = 0;

        HeapDirected<T> heap = new HeapDirected<T>(vertices);
        for (int i = 0; i < vertices; i++) {
            heap.insert(new EdgeDirected(src, i, dist[i]));
        }

        while (!heap.isEmpty()) {
            EdgeDirected<T> minEdge = heap.poll();
            int u = (int) minEdge.v2;

            for (EdgeDirected<T> neighbor : adjacent(minEdge.v2)) {
                int v = (int) neighbor.v2;
                double weight = neighbor.weight;

                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    heap.insert(new EdgeDirected<T>(minEdge.v2, neighbor.v2, dist[v]));
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
            for (EdgeDirected<T> edge : edges()) {
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
