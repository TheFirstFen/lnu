import alogrithms.graphs.DirectedGraph;

public class Main4 {
    public static void main(String[] args) {
        DirectedGraph graph = new DirectedGraph(5);

        graph.addEdge(0, 1, 2.0);
        graph.addEdge(0, 2, 4.0);
        graph.addEdge(1, 2, 1.0);
        graph.addEdge(1, 3, 7.0);
        graph.addEdge(2, 3, 3.0);
        graph.addEdge(3, 4, 1.0);

        double[] dijkstraDistances = graph.dijkstra(0);
        System.out.println("Dijkstra's Shortest Distances:");
        for (int i = 0; i < dijkstraDistances.length; i++) {
            System.out.println("From 0 to " + i + ": " + dijkstraDistances[i]);
        }

        double[] bellmanFordDistances = graph.bellmanFord(0);
        System.out.println("\nBellman-Ford's Shortest Distances:");
        for (int i = 0; i < bellmanFordDistances.length; i++) {
            System.out.println("From 0 to " + i + ": " + bellmanFordDistances[i]);
        }
    }
}
