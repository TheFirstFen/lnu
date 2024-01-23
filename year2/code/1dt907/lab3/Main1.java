import alogrithms.graphs.DirectedGraph;
import alogrithms.graphs.UndirectedGraph;

public class Main1 {
    public static void main(String[] args) {
        UndirectedGraph<Integer> undirectedGraph = new UndirectedGraph<Integer>(5);
        undirectedGraph.addEdge(0, 1, 2.5);
        undirectedGraph.addEdge(0, 2, 1.8);
        undirectedGraph.addEdge(1, 3, 3.2);
        undirectedGraph.addEdge(3, 0, 1.5);

        System.out.println("Undirected Graph:");
        System.out.println("#Vertices: " + undirectedGraph.getVertices());
        System.out.println("#Edges: " + undirectedGraph.getEdges());
        System.out.println("Edges: " + undirectedGraph.edges());
        System.out.println("Degree of vertex 0: " + undirectedGraph.degree(0));
        System.out.println("Adjacent vertices of vertex 1: " + undirectedGraph.adjacent(1));

        DirectedGraph<Integer> directedGraph = new DirectedGraph<Integer>(4);
        directedGraph.addEdge(0, 1, 2.5);
        directedGraph.addEdge(0, 2, 1.8);
        directedGraph.addEdge(1, 3, 3.2);
        directedGraph.addEdge(3, 0, 1.5);

        System.out.println("\nDirected Graph:");
        System.out.println("#Vertices: " + directedGraph.getVertices());
        System.out.println("#Edges: " + directedGraph.getEdges());
        System.out.println("Edges: " + directedGraph.edges());
        System.out.println("Degree of vertex 0: " + directedGraph.degree(0));
        System.out.println("Adjacent vertices of vertex 1: " + directedGraph.adjacent(1));
    }
}
