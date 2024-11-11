package Assignment3;

import Assignment3.Graph.Edge;

public class GraphExample {
    public static void main(String[] args) {
    UndirectedGraph undirectedGraph = new UndirectedGraph();
        undirectedGraph.addVertex(1);
        undirectedGraph.addVertex(2);
        undirectedGraph.addVertex(3);
        undirectedGraph.addEdge(1, 2);
        undirectedGraph.addEdge(2, 3);
        undirectedGraph.printGraph();

        System.out.println("#Vertices: " + undirectedGraph.getNumVertices());
        System.out.println("#Edges: " + undirectedGraph.getNumEdges());
        System.out.println("Degree of vertex 2: " + undirectedGraph.getDegree(2));

        System.out.println("Vertices: " + verticesToString(undirectedGraph.vertices()));
        System.out.println("Edges: " + edgesToString(undirectedGraph.edges()));
        System.out.println("Adjacency of vertex 2: " + adjacencyToString(undirectedGraph.adjacency(2)));

        undirectedGraph.removeEdge(1, 2);
        System.out.println("\nGraph after removing edge (1, 2):");
        undirectedGraph.printGraph();

        DirectedGraph directedGraph = new DirectedGraph();
        directedGraph.addVertex(1);
        directedGraph.addVertex(2);
        directedGraph.addVertex(3);
        directedGraph.addEdgeWithWeight(1, 2, 10);
        directedGraph.addEdgeDefaultWeight(2, 3);
        directedGraph.addEdgeDefaultWeight(1, 3);
        directedGraph.printGraph();

        System.out.println("#Vertices: " + directedGraph.getNumVertices());
        System.out.println("#Edges: " + directedGraph.getNumEdges());
        System.out.println("Degree of vertex 2: " + directedGraph.getDegree(2));

        System.out.println("Vertices: " + verticesToString(directedGraph.vertices()));
        System.out.println("Edges: " + edgesToString(directedGraph.edges()));
        System.out.println("Adjacency of vertex 2: " + adjacencyToString(directedGraph.adjacency(2)));
    }

    private static String verticesToString(Iterable<Integer> vertices) {
        StringBuilder result = new StringBuilder();
        for (int vertex : vertices) {
            result.append(vertex).append(" ");
        }
        return result.toString();
    }

    private static String edgesToString(Iterable<Graph.Edge> edges) {
        StringBuilder result = new StringBuilder();
        for (Graph.Edge edge : edges) {
            result.append(edge).append(" ");
        }
        return result.toString();
    }

    private static String adjacencyToString(Iterable<Edge> iterable) {
        StringBuilder result = new StringBuilder();
        for (Edge neighbor : iterable) {
            result.append(neighbor).append(" ");
        }
        return result.toString();
    }
}