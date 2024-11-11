package Assignment3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.HashSet;
import java.util.Set;


public class Graph {
    protected Map<Integer, List<Edge>> adjacencyList;

    public Graph() {
        this.adjacencyList = new HashMap<>();
    }

    public void addVertex(int vertex) {
        adjacencyList.put(vertex, new ArrayList<>());
    }

    public void printGraph() {
        for (Map.Entry<Integer, List<Edge>> entry : adjacencyList.entrySet()) {
            System.out.print(entry.getKey() + " -> ");
            for (Edge edge : entry.getValue()) {
                System.out.print(edge.getDestination() + " (Weight: " + edge.getWeight() + ") ");
            }
            System.out.println();
        }
    }
    public void removeEdge(int source, int destination) {
        if (!adjacencyList.containsKey(source) || !adjacencyList.containsKey(destination)) {
            throw new IllegalArgumentException("Vertices not found in the graph");
        }

        List<Edge> edges = adjacencyList.get(source);
        edges.removeIf(edge -> edge.getDestination() == destination);
    }

    public int getNumVertices() {
        return adjacencyList.size();
    }

    public int getNumEdges() {
        int count = 0;
        for (List<Edge> edges : adjacencyList.values()) {
            count += edges.size();
        }
        return count;
    }

    public int getDegree(int vertex) {
        if (!adjacencyList.containsKey(vertex)) {
            throw new IllegalArgumentException("Vertex not found in the graph");
        }

        return adjacencyList.get(vertex).size();
    }
    public Iterable<Integer> vertices() {
        return adjacencyList.keySet();
    }

    public Iterable<Edge> edges() {
        List<Edge> allEdges = new ArrayList<>();
        for (List<Edge> edges : adjacencyList.values()) {
            allEdges.addAll(edges);
        }
        return allEdges;
    }

    public Iterable<Edge> adjacency(int vertex) {
        if (!adjacencyList.containsKey(vertex)) {
            throw new IllegalArgumentException("Vertex not found in the graph");
        }
        return adjacencyList.get(vertex);
    }

    public static class Edge {
        private int source;
        private int destination;
        private double weight;

        public Edge(int sourc, int destinatio, double weigh) {
            source = sourc;
            destination = destinatio;
            weight = weigh;
        }

        public int getSource() {
            return source;
        }

        public int getDestination() {
            return destination;
        }

        public double getWeight() {
            return weight;
        }

        @Override
        public String toString() {
            return "(" + source + " -> " + destination + " | Weight: " + weight + ")";
        }
    }

    public Iterable<List<Edge>> kruskal() {
        PQAsHeap minHeap = new PQAsHeap();
        for (Map.Entry<Integer, List<Edge>> entry : adjacencyList.entrySet()) {
            List<Edge> edges = entry.getValue();
            for (Edge edge : edges) {
                minHeap.insert_person(edge.getSource() + "_" + edge.getDestination(), edge.getWeight());
                minHeap.insert_person(edge.getDestination() + "_" + edge.getSource(), edge.getWeight());
            }
        }
        
        UF uf = new UF(adjacencyList.size() + 1);
        List<List<Edge>> minimalSpanningForest = new ArrayList<>();
        Set<Integer> visitedVertices = new HashSet<>();
        
        while (!minHeap.isEmpty() && visitedVertices.size() <= adjacencyList.size()) {
            List<Edge> minimalSpanningTree = new ArrayList<>();
            
            while (!minHeap.isEmpty()) {
                String edgeInfo = minHeap.get_person().getName();
                int source = Integer.parseInt(edgeInfo.split("_")[0]);
                int destination = Integer.parseInt(edgeInfo.split("_")[1]);
                double weight = minHeap.get_person().getPrio();
    
                if (!uf.connected(source, destination)) {
                    uf.union(source, destination);
                    minimalSpanningTree.add(new Edge(source, destination, weight));
                    visitedVertices.add(source);
                    visitedVertices.add(destination);
                    break;
                }
            }
    
            mergeMSTs(minimalSpanningForest, minimalSpanningTree);
            
            if (!minimalSpanningTree.isEmpty()) {
                minimalSpanningForest.add(minimalSpanningTree);
            }
        }
    
        return minimalSpanningForest;
    }
    
    private void mergeMSTs(List<List<Edge>> forest, List<Edge> newTree) {
        for (List<Edge> existingMST : forest) {
            for (Edge edge : existingMST) {
                if (edgeConnectsToTree(edge, newTree)) {
                    newTree.addAll(existingMST);
                    forest.remove(existingMST);
                    return;
                }
            }
        }
    }
    
    private boolean edgeConnectsToTree(Edge edge, List<Edge> tree) {
        return tree.stream().anyMatch(e -> e.getSource() == edge.getSource() || e.getDestination() == edge.getSource()) ||
                tree.stream().anyMatch(e -> e.getSource() == edge.getDestination() || e.getDestination() == edge.getDestination());
    }
    public double[] dijkstra(int src) {
        double[] dist = new double[adjacencyList.size()];
        Arrays.fill(dist, Double.POSITIVE_INFINITY);
        dist[src - 1] = 0;
    
        PQAsHeap heap = new PQAsHeap();
        heap.insert_person(src + "_" + src, 0);
    
        while (!heap.isEmpty()) {
            HeapNode minEdge = heap.get_person();
            int u = Integer.parseInt(minEdge.getName().split("_")[0]);
            double minDist = minEdge.getPrio();
    
            if (minDist > dist[u - 1]) {
                continue;
            }
    
            for (Edge neighbor : adjacencyList.get(u)) {
                int v = neighbor.destination;
                double weight = neighbor.weight;
    
                if (dist[u - 1] + weight < dist[v - 1]) {
                    dist[v - 1] = dist[u - 1] + weight;
                    heap.insert_person(v + "_" + v, dist[v - 1]);
                }
            }
        }
        return dist;
    }
    
    

    
    public double[] bellmanFord(int src) {
        double[] dist = new double[adjacencyList.size() + 1];
        Arrays.fill(dist, Double.POSITIVE_INFINITY);
        dist[src - 1] = 0;
    
        for (int i = 0; i < adjacencyList.size(); i++) {
            for (List<Edge> edges : adjacencyList.values()) {
                for (Edge edge : edges) {
                    int u = edge.source - 1;
                    int v = edge.destination - 1;
                    double weight = edge.weight;
    
                    if (dist[u] + weight < dist[v]) {
                        dist[v] = dist[u] + weight;
                    }
                }
            }
        }
    
        return dist;
    }
}
