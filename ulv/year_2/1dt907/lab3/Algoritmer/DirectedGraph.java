package Algoritmer;

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class DirectedGraph extends Graph {
    public DirectedGraph(int vertices) {
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
    }

    @Override
    public void removeEdge(int start, int end) {
        adj.get(start).removeIf(edge -> edge.end == end);
    }

    @Override
    public int degree(int vertex) {
        return adj.get(vertex).size();
    }

    @Override
    public void display() {
        System.out.println("\nDirected Graph:");
        for (int i = 0; i < vertices; i++) {
            System.out.print("Vertex " + i + " is connected to: ");
            for (Edge edge : adj.get(i)) {
                System.out.print("(" + edge.start + " -> " + edge.end + " w:" + edge.weight + ") ");
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

    public double[] bellmanFord(int src) {
        double[] dist = new double[vertices];
        Arrays.fill(dist, Double.MAX_VALUE);
        dist[src] = 0;

        for (int i = 0; i < vertices - 1; i++) {
            for (int j = 0; j < vertices; j++) {
                for (Edge edge : adj.get(j)) {
                    if (dist[j] != Double.MAX_VALUE && dist[j] + edge.weight < dist[edge.end]) {
                        dist[edge.end] = dist[j] + edge.weight;
                    }
                }
            }
        }

        for (int i = 0; i < vertices; i++) {
            for (Edge edge : adj.get(i)) {
                if (dist[i] != Double.MAX_VALUE && dist[i] + edge.weight < dist[edge.end]) {
                    System.err.println("Graph contains negative weight cycle");
                    return null;
                }
            }
        }

        //System.out.println("Shortest distances from source vertex " + src);
        //for (int i = 0; i < vertices; i++) {
            //System.out.println("Vertex " + i + ": " + dist[i]);
        //}
        return dist;
    }

    public void displaybellmanFord(double[] dist, int src) {
        System.out.println("Shortest distances from source vertex " + src);
        for (int i = 0; i < vertices; i++) {
            System.out.println("Vertex " + i + ": " + dist[i]);
        }
    }
}
