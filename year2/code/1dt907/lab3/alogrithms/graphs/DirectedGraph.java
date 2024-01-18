package alogrithms.graphs;

import java.util.List;

import alogrithms.Heap;

import java.util.ArrayList;
import java.util.Arrays;

public class DirectedGraph extends Graph {
    private List<List<Edge>> adjacencyList;

    public DirectedGraph(int vertices) {
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
    }

    @Override
    public void removeEdge(int v, int w) {
        super.removeEdge(v, w);
        adjacencyList.get(v).removeIf(edge -> edge.v2 == w);
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
            edgesList.addAll(adjacencyList.get(v));
        }
        return edgesList;
    }

    @Override
    public Iterable<Edge> adjacent(int v) {
        return adjacencyList.get(v);
    }

    // * Uppgift 2
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

    // * Uppgift 4
    public double[] dijkstra(int source) {
        double[] dist = new double[vertices];
        Arrays.fill(dist, Double.POSITIVE_INFINITY);
        dist[source] = 0;

        Heap minHeap = new Heap(vertices);
        for (int i = 0; i < vertices; i++) {
            minHeap.insert(new Edge(source, i, dist[i]));
        }

        while (!minHeap.isEmpty()) {
            Edge minEdge = minHeap.poll();
            int u = minEdge.v2;

            for (Edge neighbor : adjacent(u)) {
                int v = neighbor.v2;
                double weight = neighbor.weight;

                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    minHeap.insert(new Edge(u, v, dist[v]));
                }
            }
        }

        return dist;
    }

    public double[] bellmanFord(int source) {
        double[] dist = new double[vertices];
        Arrays.fill(dist, Double.POSITIVE_INFINITY);
        dist[source] = 0;

        for (int i = 1; i < vertices - 1; i++) {
            for (Edge edge : edges()) {
                int u = edge.v1;
                int v = edge.v2;
                double weight = edge.weight;

                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                }
            }
        }

        return dist;
    }

    // * Uppgift 5
    public List<Integer> topologicalSort() {
        boolean[] visited = new boolean[vertices];
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < vertices; i++) {
            if (!visited[i]) {
                topologicalSortUtil(i, visited, result);
            }
        }

        List<Integer> reversedResult = new ArrayList<>(result);
        java.util.Collections.reverse(reversedResult);
        return reversedResult;
    }

    private void topologicalSortUtil(int vertex, boolean[] visited, List<Integer> result) {
        visited[vertex] = true;

        for (Edge edge : adjacencyList.get(vertex)) {
            int n = edge.v2;
            if (!visited[n]) {
                topologicalSortUtil(n, visited, result);
            }
        }

        result.add(vertex);
    }
}
