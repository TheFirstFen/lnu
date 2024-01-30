import alogrithms.graphs.DirectedGraph;
import alogrithms.graphs.UndirectedGraph;

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
        // System.out.println("Dijkstra's Shortest Distances:");
        // for (int i = 0; i < dijkstraDistances.length; i++) {
        // System.out.println("From 0 to " + i + ": " + dijkstraDistances[i]);
        // }

        sw.stop();
        double directedDjikstaraTime = sw.getTimeInNanoSeconds();
        sw.reset();

        sw.start();

        double[] bellmanFordDistances = directedGraph.bellmanFord(0);
        // System.out.println("\nBellman-Ford's Shortest Distances:");
        // for (int i = 0; i < bellmanFordDistances.length; i++) {
        // System.out.println("From 0 to " + i + ": " + bellmanFordDistances[i]);
        // }

        sw.stop();
        double directedBellmanFordTime = sw.getTimeInNanoSeconds();
        sw.reset();

        UndirectedGraph<Integer> undirectedGraph = new UndirectedGraph<Integer>(10_001);

        for (int i = 0; i < 10_000; i++) {
            undirectedGraph.addEdge(i, i + 1, rnd.nextDouble());
        }

        for (int i = 0; i < 10_000; i++) {
            undirectedGraph.addEdge(rnd.nextInt(10_000), rnd.nextInt(10_000), rnd.nextDouble());
        }

        sw.start();

        dijkstraDistances = undirectedGraph.dijkstra(0);
        // System.out.println("\nDijkstra's Shortest Distances:");
        // for (int i = 0; i < dijkstraDistances.length; i++) {
        // System.out.println("From 0 to " + i + ": " + dijkstraDistances[i]);
        // }

        sw.stop();
        double undirectedDjikstaraTime = sw.getTimeInNanoSeconds();
        sw.reset();

        sw.start();// ???? Felaktigt ?

        bellmanFordDistances = undirectedGraph.bellmanFord(0);
        // System.out.println("\nBellman-Ford's Shortest Distances:");
        // for (int i = 0; i < bellmanFordDistances.length; i++) {
        // System.out.println("From 0 to " + i + ": " + bellmanFordDistances[i]);
        // }

        sw.stop();
        double undirectedBellmanFordTime = sw.getTimeInNanoSeconds();
        sw.reset();

        System.out.println("\n\nDirected graph:");
        System.out.println("Dijkstra's Time: " + sw.chooseTimePrefix(directedDjikstaraTime));
        System.out.println("Bellman-Ford's Time: " + sw.chooseTimePrefix(directedBellmanFordTime));

        System.out.println("\n\nUndirected graph:");
        System.out.println("Dijkstra's Time: " + sw.chooseTimePrefix(undirectedDjikstaraTime));
        System.out.println("Bellman-Ford's Time: " + sw.chooseTimePrefix(undirectedBellmanFordTime));
    }
}
