package Assignment3;

import java.util.List;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;



public class UndirectedGraph extends Graph{

    public void addEdgeDefaultWeight(int source, int destination) {
        addEdgeWithWeight(source, destination, 1.0);
        adjacencyList.get(destination).add(new Edge(destination, source, 1.0));
    }

    public void addEdgeWithWeight(int source, int destination, double weight) {
        if (!adjacencyList.containsKey(source) || !adjacencyList.containsKey(destination)) {
            throw new IllegalArgumentException("Vertices not found in the graph");
        }
        adjacencyList.get(source).add(new Edge(source, destination, weight));
        adjacencyList.get(destination).add(new Edge(destination, source, weight));
    }

    public void addEdge(int source, int destination) {
        addEdgeWithWeight(source, destination, 0.0);
        adjacencyList.get(destination).add(new Edge(destination, source, 0.0));
    }
    @Override
    public void removeEdge(int source, int destination) {
        super.removeEdge(source, destination);

        // For undirected graph, remove the reverse edge as well
        adjacencyList.get(destination).removeIf(edge -> edge.getDestination() == source);
    }
    
    @Override
    public int getNumEdges() {
        int count = 0;
        for (List<Edge> edges : adjacencyList.values()) {
            count += edges.size();
        }
        return count / 2;
    }
    public Iterable<Integer> dfs(int startVertex) {
        Set<Integer> visited = new HashSet<>();
        List<Integer> traversal = new ArrayList<>();
        dfsHelper(startVertex, visited, traversal);
        return traversal;
    }

    public Iterable<Integer> bfs(int startVertex) {
        Set<Integer> visited = new HashSet<>();
        List<Integer> traversal = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();

        visited.add(startVertex);
        queue.add(startVertex);

        while (!queue.isEmpty()) {
            int current = queue.poll();
            traversal.add(current);

            for (Edge edge : adjacencyList.get(current)) {
                int neighbor = edge.getDestination();
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                }
            }
        }

        return traversal;
    }
    private void dfsHelper(int vertex, Set<Integer> visited, List<Integer> traversal) {
        visited.add(vertex);
        traversal.add(vertex);

        for (Edge edge : adjacencyList.get(vertex)) {
            int neighbor = edge.getDestination();
            if (!visited.contains(neighbor)) {
                dfsHelper(neighbor, visited, traversal);
            }
        }
    }

    
}
