package Assignment3;

import java.util.ArrayList;
import java.util.List;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;

public class DirectedGraph extends Graph {
    public void addEdgeDefaultWeight(int source, int destination) {
        addEdgeWithWeight(source, destination, 1.0);
    }


    public void addEdgeWithWeight(int source, int destination, double weight) {
        if (!adjacencyList.containsKey(source) || !adjacencyList.containsKey(destination)) {
            throw new IllegalArgumentException("Vertices not found in the graph");
        }
        Edge nEdge = new Edge(source, destination, weight);
        adjacencyList.get(source).add(nEdge);
    }
    @Override
    public int getDegree(int vertex) {
        if (!adjacencyList.containsKey(vertex)) {
            throw new IllegalArgumentException("Vertex not found in the graph");
        }

        return adjacencyList.get(vertex).size() * 2;
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
        LinkedList<Integer> queue = new LinkedList<>();

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
