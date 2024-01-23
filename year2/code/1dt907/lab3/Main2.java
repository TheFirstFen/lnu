import alogrithms.graphs.DirectedGraph;
import alogrithms.graphs.UndirectedGraph;

public class Main2 {
    public static void main(String[] args) {
        UndirectedGraph<Integer> undirectedGraph = new UndirectedGraph<Integer>(11);

        undirectedGraph.addEdge(0, 1);
        undirectedGraph.addEdge(1, 2);
        undirectedGraph.addEdge(2, 3);
        undirectedGraph.addEdge(3, 4);
        undirectedGraph.addEdge(10, 5);
        undirectedGraph.addEdge(5, 3, 4.0);
        undirectedGraph.addEdge(0, 10, 4.0);
        undirectedGraph.addEdge(1, 6);

        System.out.println("DFS Treversal:");
        undirectedGraph.dfs(0);

        System.out.println("\n\nBFS Treversal:");
        undirectedGraph.bfs(0);

        System.out.println("\n\nIs 0 - 10 connected: " + undirectedGraph.isConnected(0, 10));

        System.out.println("\nOne path from 0 - 10: " + undirectedGraph.path(0, 10));

        DirectedGraph<Integer> directedGraph = new DirectedGraph<Integer>(11);

        directedGraph.addEdge(0, 1);
        directedGraph.addEdge(1, 2);
        directedGraph.addEdge(2, 3);
        directedGraph.addEdge(3, 4);
        directedGraph.addEdge(10, 5);
        directedGraph.addEdge(5, 3, 2.0);
        directedGraph.addEdge(10, 3, 4.0);

        System.out.println("\n\nDFS Treversal:");
        directedGraph.dfs(0);

        System.out.println("\n\nBFS Treversal:");
        directedGraph.bfs(0);

        System.out.println("\n\nIs 0 - 10 connected: " + directedGraph.isConnected(0, 10));

        System.out.println("\nOne path from 0 - 10: " + directedGraph.path(0, 10));
    }
}
