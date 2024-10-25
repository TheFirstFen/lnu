package Algoritmer;

import java.util.ArrayList;
import java.util.List;

import java.util.Arrays;

public class UndirectedGraph extends Graph {
    public UndirectedGraph(int vertices) {
        super(vertices);
    }

    @Override
    public int getVertices() {
        return vertices;
    }

    public void addEdge(int start, int end) {
        addEdge(start, end, 1.0);
    }

    @Override
    public void addEdge(int start, int end, double weight) {
        adj.get(start).add(new Edge(start, end, weight));
        adj.get(end).add(new Edge(end, start, weight));
    }

    @Override
    public void removeEdge(int start, int end) {
        adj.get(start).removeIf(edge -> edge.end == end);
        adj.get(end).removeIf(edge -> edge.end == start);
    }

    @Override
    public int degree(int vertex) {
        return adj.get(vertex).size();
    }

    @Override
    public void display() {
        System.out.println("\nUndirected Graph:");
        for (int i = 0; i < vertices; i++) {
            System.out.print("Vertex " + i + " is connected to: ");
            for (Edge edge : adj.get(i)) {
                System.out.print("(" + edge.start + " - " + edge.end + " w:" + edge.weight + ") ");
            }
            System.out.println();
        }
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
        for (int i = 0; i < vertices; i++) {
            for (Edge edge : adj.get(i)) {
                if (i < edge.end) {
                    edgesList.add(new Edge(i, edge.end, edge.weight));
                }
                edgesList.add(edge);
            }
        }
        return edgesList;
    }

    @Override
    public Iterable<Edge> adjacency(int vertex) {
        return adj.get(vertex);
    }

    @Override
    public String toString() {
        String result = "\nUndirected Graph:";
        for (int i = 0; i < vertices; i++) {
            result += "\n" + adjacencyToString(i);
        }
        return result;
    }

    @Override
    public void dfs(int startVertex) {
        Boolean[] visited = new Boolean[vertices];
        for(int i = 0; i < vertices; i++) {
            visited[i] = false;
        }

        List<Integer> stack = new ArrayList<>();       

        dfsrecursive(startVertex, visited, stack);

        for(int vertex : stack) {
            System.out.println(vertex + " ");
        }
        System.out.println();
    }

    private void dfsrecursive(int vertex, Boolean[] visited, List<Integer> stack) {
        visited[vertex] = true;
        stack.add(vertex);

        for (Edge edge : adj.get(vertex)) {
            int next = edge.end;
            if (!visited[next]) {
                dfsrecursive(next, visited, stack);
            }
        }
    }

    @Override
    public void bfs(int startVertex) {
        boolean[] visited = new boolean[vertices];
        List<Integer> queue = new ArrayList<>();

        visited[startVertex] = true;
        queue.add(startVertex);
        int front = 0;
        
        while (front < queue.size()) {
            int currentVertex = queue.get(front++);
            System.out.println(currentVertex + " ");

            for (Edge edge : adj.get(currentVertex)) {
                int next = edge.end;
                if (!visited[next]) {
                    visited[next] = true;
                    queue.add(next);
                }
            }
        }
        System.out.println();
    }

    public class Dijkstra {

        protected final int V;
        private final List<List<Edge>> adj;

        public Dijkstra(int V) {
            this.V = V;
            adj = new ArrayList<>();
            for (int i = 0; i < V; ++i) {
                adj.add(new ArrayList<>());
            }
        }

        public int getVertex() {
            return V;
        }

        public void addEdge(int u, int v, double w) {
            adj.get(u).add(new Edge(u, v, w));
            adj.get(v).add(new Edge(v, u, w));
        }

        public double[] shortestPath(int src) {
            double[] dist = new double[V];
            int[] pred = new int[V];
            boolean[] visited = new boolean[V];

            Arrays.fill(dist, Double.MAX_VALUE);
            Arrays.fill(pred, -1);
            dist[src] = 0;

            for (int i = 0; i < V; ++i) {
                int u = minDistance(dist, visited);
                visited[u] = true;

                for (Edge e : adj.get(u)) {
                    int v = e.end;
                    double weight = e.weight;
                    if (!visited[v] && weight != Double.MAX_VALUE && dist[u] + weight < dist[v]) {
                        dist[v] = dist[u] + weight;
                        pred[v] = u;
                    }
                }
            }

            return dist;
        }

        private int minDistance(double[] dist, boolean[] visited) {
            double min = Double.MAX_VALUE;
            int minIndex = -1;

            for (int i = 0; i < V; i++) {
                if (!visited[i] && dist[i] <= min) {
                    min = dist[i];
                    minIndex = i;
                }
            }
            return minIndex;
        }
    }
}
