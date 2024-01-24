import alogrithms.graphs.DirectedGraph;

import java.util.Random;

public class Main4 {
    public static void main(String[] args) {
        DirectedGraph<Integer> graph = new DirectedGraph<Integer>(30);

        graph.addEdge(0, 1, 2.0);
        graph.addEdge(0, 2, 4.0);
        graph.addEdge(1, 2, 1.0);
        graph.addEdge(1, 3, 7.0);
        graph.addEdge(2, 3, 3.0);
        graph.addEdge(3, 4, 1.0);

        Random random = new Random();

        for (int i = 0; i < 30; i++) {
            double weight1 = random.nextInt(1000) * 0.15;
            double weight2 = random.nextInt(1000) * 0.15;

            graph.addEdge(i, (i + 1) % 30, weight1);
            graph.addEdge(i, (i + 2) % 30, weight2);
        }

        for (int i = 0; i < 20; i++) {
            double additionalWeight1 = random.nextInt(1000) * 0.15;
            double additionalWeight2 = random.nextInt(1000) * 0.15;

            graph.addEdge(i, (i + 5) % 30, additionalWeight1);
            graph.addEdge((i + 15) % 30, (i + 20) % 30, additionalWeight2);
        }

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
