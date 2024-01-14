import alogrithms.graphs.DirectedGraph;
import alogrithms.graphs.UndirectedGraph;

public class Main1 {
    public static void main(String[] args) {
        // Example for UndirectedGraph
        UndirectedGraph undirectedGraph = new UndirectedGraph(5);
        undirectedGraph.addEdge(0, 1);
        undirectedGraph.addEdge(0, 2);
        undirectedGraph.addEdge(1, 3);
        undirectedGraph.addEdge(4, 0);

        System.out.println("Undirected Graph:");
        System.out.println("#Vertices: " + undirectedGraph.getVertices());
        System.out.println("#Edges: " + undirectedGraph.getEdges());
        System.out.println("Edges: " + undirectedGraph.edges());
        System.out.println("Degree of vertex 0: " + undirectedGraph.degree(0));
        System.out.println("Adjacent vertices of vertex 1: " + undirectedGraph.adjacent(1));

        // Example for DirectedGraph
        DirectedGraph directedGraph = new DirectedGraph(4);
        directedGraph.addEdge(0, 1);
        directedGraph.addEdge(0, 2);
        directedGraph.addEdge(1, 3);
        directedGraph.addEdge(3, 0);

        System.out.println("\nDirected Graph:");
        System.out.println("#Vertices: " + directedGraph.getVertices());
        System.out.println("#Edges: " + directedGraph.getEdges());
        System.out.println("Edges: " + directedGraph.edges());
        System.out.println("Degree of vertex 0: " + directedGraph.degree(0));
        System.out.println("Adjacent vertices of vertex 1: " + directedGraph.adjacent(1));
    }
}
