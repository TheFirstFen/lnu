import alogrithms.graphs.DirectedGraph;
import alogrithms.graphs.Edge;
import alogrithms.graphs.UndirectedGraph;

public class Main2 {
    public static void main(String[] args) {
        UndirectedGraph undirectedGraph = new UndirectedGraph(11);

        undirectedGraph.addEdge(0, 1);
        undirectedGraph.addEdge(1, 2);
        undirectedGraph.addEdge(2, 3);
        undirectedGraph.addEdge(3, 4);
        undirectedGraph.addEdge(10, 5);
        undirectedGraph.addEdge(5, 3, 4.0);
        undirectedGraph.addEdge(0, 10, 4.0);

        System.out.println("Undirected graph edges:");
        for (Edge edge : undirectedGraph.edges()) {
            System.out.println(edge);
        }

        int source = 0;
        int destination = 5;

        boolean isConnected = undirectedGraph.isConnected(source, destination);
        System.out.println("Is " + source + " connected to " + destination + "? " + isConnected);

        Iterable<Integer> path = undirectedGraph.path(source, destination);
        System.out.println("Path from " + source + " to " + destination + ": " + path);

        DirectedGraph directedGraph = new DirectedGraph(11);

        directedGraph.addEdge(0, 1);
        directedGraph.addEdge(1, 2);
        directedGraph.addEdge(2, 3);
        directedGraph.addEdge(3, 4);
        directedGraph.addEdge(10, 5);
        directedGraph.addEdge(5, 3, 2.0);
        directedGraph.addEdge(10, 3, 4.0);

        System.out.println("\nDirected graph edges:");
        for (Edge edge : directedGraph.edges()) {
            System.out.println(edge);
        }

        source = 10;
        destination = 3;

        isConnected = directedGraph.isConnected(source, destination);
        System.out.println("Is " + source + " connected to " + destination + "? " + isConnected);

        path = directedGraph.path(source, destination);
        System.out.println("Path from " + source + " to " + destination + ": " + path);
    }
}
