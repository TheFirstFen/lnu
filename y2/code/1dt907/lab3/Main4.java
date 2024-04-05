import alogrithms.graphs.DirectedGraph;

import java.util.Random;

public class Main4 {
    public static void main(String[] args) {
        Random rnd = new Random();
        Timer sw = new Timer();

        DirectedGraph<Integer> directedGraph = new DirectedGraph<Integer>(10_001);

        for (int i = 0; i < 10_000; i++) {
            directedGraph.addEdge(i, i + 1, rnd.nextDouble());
        }

        for (int i = 0; i < 10_000; i++) {
            directedGraph.addEdge(rnd.nextInt(10_000), rnd.nextInt(10_000), rnd.nextDouble());
        }

        sw.start();

        double[] dijkstraDistances = directedGraph.dijkstra(0);

        sw.stop();

        System.out.println("Dijkstra's Shortest Distances sample:");
        for (int i = 0; i < dijkstraDistances.length / 1_000; i++) {
            int sample = rnd.nextInt(dijkstraDistances.length);
            System.out.println("From 0 to " + sample + ": " + dijkstraDistances[sample]);
        }

        System.out.println("\nDijkstra's Time: " + sw.chooseTimePrefix(sw.getTimeInNanoSeconds()));
        sw.reset();
        sw.start();

        double[] bellmanFordDistances = directedGraph.bellmanFord(0);

        sw.stop();

        System.out.println("\nBellman-Ford's Shortest Distances sample:");
        for (int i = 0; i < bellmanFordDistances.length / 1_000; i++) {
            int sample = rnd.nextInt(bellmanFordDistances.length);
            System.out.println("From 0 to " + sample + ": " + bellmanFordDistances[sample]);
        }

        System.out.println("\nBellman-Ford's Time: " + sw.chooseTimePrefix(sw.getTimeInNanoSeconds()));
        sw.reset();
    }
}
