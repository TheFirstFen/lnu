package Algoritmer;

import java.util.List;
import java.util.ArrayList;

public abstract class Graph {
    protected int vertices;
    protected List<List<Edge>> adj;

    public Graph(int vertices) {
        this.vertices = vertices;
        this.adj = new ArrayList<>();
        for (int i = 0; i < vertices; i++) {
            adj.add(new ArrayList<>());
        }
    }

    public int getTotalEdges() {
        int total = 0;
        for (List<Edge> edges : adj) {
            total += edges.size();
        }
        return this instanceof UndirectedGraph ? total / 2 : total;
    }

    public abstract int getVertices();

    public abstract void addEdge(int start, int end, double weight);

    public abstract void removeEdge(int start, int end);

    public abstract int degree(int vertex);

    public abstract void display();

    public abstract Iterable<Integer> vertices ();

    public abstract Iterable<Edge> edges ();

    public abstract Iterable<Edge> adjacency (int vertex);

    public abstract void dfs(int startVertex);

    public abstract void bfs(int startVertex);

    public String edgeToString(Edge edge) {
        return edge.toString();
    }

    public String adjacencyToString(int vertex) {
        String result = "Vertex " + vertex + " is connected to: ";
        for (Edge edge : adj.get(vertex)) {
            result += edgeToString(edge) + " ";
        }
        return result;
    }

    public class Edge {
        public int start;
        public int end;
        public double weight;

        public Edge(int start, int end, double weight) {
            this.start = start;
            this.end = end;
            this.weight = weight;
        }

        @Override 
        public String toString() {
            return "(" + this.start + " - " + this.end + " w:" + this.weight + ")";
        }
    }

    public static void main(String[] args) {
        UndirectedGraph graph = new UndirectedGraph(5);
        System.out.println("Number of vertices: " + graph.getVertices());
        System.out.println("Number of edges: " + graph.getTotalEdges());
        System.out.println("Adding 3 edges:");
        graph.addEdge(0, 1);
        graph.addEdge(0, 2, 1.5);
        graph.addEdge(1, 2, 2.0);
        graph.addEdge(4, 2);
        graph.addEdge(3, 4);
        graph.addEdge(0, 3);
        System.out.println("Number of edges: " + graph.getTotalEdges());

        graph.display();
        System.out.println("Vertex 0 has " + graph.degree(0) + " edges\n");
        System.out.println("Removing edge (0, 2)");
        graph.removeEdge(0, 2);
        graph.display();

        System.out.println("Iterable: " + graph.vertices());
        System.out.println("Iterable: " + graph.edges());
        System.out.println("Iterable: " + graph.adjacency(0));

        DirectedGraph directedGraph = new DirectedGraph(5);
        directedGraph.addEdge(0, 1, 1.0);
        directedGraph.addEdge(0, 2, 1.6);
        directedGraph.addEdge(1, 2, 2.1);
        directedGraph.addEdge(4, 2);
        directedGraph.addEdge(3, 4);
        directedGraph.addEdge(0, 3);
        System.out.println("Number of edges: " + directedGraph.getTotalEdges());

        directedGraph.display();
        System.out.println("Vertex 0 has " + directedGraph.degree(0) + " edges\n");
        System.out.println("Removing edge (0, 2)");
        directedGraph.removeEdge(0, 2);
        directedGraph.display();
        System.out.println("Iterable: " + directedGraph.vertices());
        System.out.println("Iterable: " + directedGraph.edges());
        System.out.println("Iterable: " + directedGraph.adjacency(0));
        System.out.println("Number of edges: " + directedGraph.getTotalEdges());

        System.out.println("\nDFS:");
        System.out.println("Undirected Graph:");
        graph.dfs(0);
        System.out.println("Directed Graph:");
        directedGraph.dfs(0);

        System.out.println("BFS:");
        System.out.println("Undirected Graph:");
        graph.bfs(0);
        System.out.println("Directed Graph:");
        directedGraph.bfs(0);

        UndirectedGraph graphs = new UndirectedGraph(5);
        graphs.addEdge(0, 1, 2.1);
        graphs.addEdge(0, 2, 3.2);
        graphs.addEdge(1, 2, 1.2);
        graphs.addEdge(1, 3, 1.5);
        graphs.addEdge(2, 3, 4.3);
        graphs.addEdge(3, 4, 2.2);

        List<Graph.Edge> minimumSpanningTree = Kruskal.kruskal(graphs);

        System.out.println("Kruskals Algorithm:");
        System.out.println("Minimum Spanning Tree Edges:");
        for (Graph.Edge edge : minimumSpanningTree) {
            System.out.println(edge);
        }

        System.out.println("Djikstras Algorithm:");

        System.out.println("Bellman-Ford Algorithm:");
   
    }
}
