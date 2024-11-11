package Assignment3;

import java.util.*;

public class ShortestPath {
    public static void main(String[] args) {
        DirectedGraph directedGraph = new DirectedGraph();

        int[] amountOfVertices = {100, 500, 1000, 5000};
        int[] amountOfEdges = {5000, 10000, 20000, 30000};

        for (int vert = 0;vert < amountOfVertices.length; vert++) {
            System.out.println("\nTiming with " + amountOfVertices[vert] + " vertices:");
            for (int edg = 0;edg < amountOfEdges.length; edg++) {
                System.out.println(amountOfEdges[edg] + " edges:");

                for (int i = 1; i < amountOfVertices[vert]; i++) {
                    directedGraph.addVertex(i);
                }

                Random random = new Random();

                for (int j = 0; j < amountOfEdges[edg]; j++) {
                    int source = random.nextInt(amountOfVertices[vert] - 1) + 1;
                    int destination = random.nextInt(amountOfVertices[vert] - 1) + 1;
                    int weight = random.nextInt(100);
                    directedGraph.addEdgeWithWeight(source, destination, weight);
                }

                System.out.print("Dijkstra Algorithm: ");
                Runnable c = () -> directedGraph.dijkstra(1);
                Timeit.timeCode(c, 1, true);
                // int src = 1;
                // double[] dijkstraDistances = directedGraph.dijkstra(src);
                // for (int i = 0; i < dijkstraDistances.length; i++) {
                //     System.out.println("Shortest distance from node " + src + " to node " + (i + 1) + ": " + dijkstraDistances[i]);
                // }
                
                
                
                System.out.print("Bellman-Ford Algorithm: ");
                Runnable r = () -> directedGraph.bellmanFord(1);
                Timeit.timeCode(r, 1, true);
                // src = 1;
                // double[] bellmanFordDistances = directedGraph.bellmanFord(src);
                // for (int i = 0; i < bellmanFordDistances.length - 1; i++) {
                //     System.out.println("Shortest distance from node " + src + " to node " + (i + 1) + ": " + bellmanFordDistances[i]);
                // }
            }
        }
    }
}

