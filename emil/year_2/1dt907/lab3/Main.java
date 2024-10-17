import java.util.*;

import Algoritmer.*;
import Algoritmer.Timer;

public class Main {
    public static void main(String[] args) {
        System.out.println("Problem 1");
        UndirectedGraph graph = new UndirectedGraph(5);
        graph.addEdge(0, 1);
        graph.addEdge(0, 2, 1.5);
        graph.addEdge(1, 2, 2.0);
        graph.addEdge(4, 2);
        graph.addEdge(3, 4);
        graph.addEdge(0, 3);

        graph.display();
        System.out.println("Vertex 0 has " + graph.degree(0) + " edges\n");
        System.out.println("Removing edge (0, 2)");
        graph.removeEdge(0, 2);
        graph.display();

        System.out.println("\nIterable vertices: " + graph.vertices());
        System.out.println("Iterable edges: " + graph.edges());
        System.out.println("Iterable adjacency: " + graph.adjacency(0));

        DirectedGraph directedGraph = new DirectedGraph(5);
        directedGraph.addEdge(0, 1, 1.0);
        directedGraph.addEdge(0, 2, 1.6);
        directedGraph.addEdge(1, 2, 2.1);
        directedGraph.addEdge(4, 2);
        directedGraph.addEdge(3, 4);
        directedGraph.addEdge(0, 3);

        directedGraph.display();
        System.out.println("Vertex 0 has " + directedGraph.degree(0) + " edges\n");
        System.out.println("Removing edge (0, 2)");
        directedGraph.removeEdge(0, 2);
        directedGraph.display();

        System.out.println("\nIterable vertices: " + directedGraph.vertices());
        System.out.println("Iterable edges: " + directedGraph.edges());
        System.out.println("Iterable adjacency: " + directedGraph.adjacency(0));

        System.out.println("\nProblem 2");
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

        System.out.println("\nProblem 3");
        UndirectedGraph graphs = new UndirectedGraph(15);
        graphs.addEdge(0, 1, 2.1);
        graphs.addEdge(0, 2, 3.2);
        graphs.addEdge(1, 2, 1.2);
        graphs.addEdge(1, 3, 1.5);
        graphs.addEdge(2, 3, 4.3);
        graphs.addEdge(3, 4, 2.2);

        graphs.addEdge(10, 11, 2.1);
        graphs.addEdge(13, 12, 1.1);
        graphs.addEdge(11, 13);
        graphs.addEdge(10, 14, 2.5);

        List<Graph.Edge> minimumSpanningTree = Kruskal.kruskal(graphs);

        System.out.println("Kruskals Algorithm:");

        List<List<Graph.Edge>> connectedComponents = Kruskal.groupEdgesByConnectedComponents(minimumSpanningTree, graphs.getVertices());

        for (List<Graph.Edge> componentEdges : connectedComponents) {
            if (!componentEdges.isEmpty()) {
                System.out.println("Minimum Spanning Tree:");
                for (Graph.Edge edge : componentEdges) {
                    System.out.println(edge);
                }
                System.out.println();
            }
        }

        System.out.println("\nProblem 4");
        System.out.println("Djikstras Algorithm:");

        int numVertices = 5;
        UndirectedGraph graphdDijkstra = new UndirectedGraph(numVertices);

        graphdDijkstra.addEdge(0, 1, 1.5);
        graphdDijkstra.addEdge(0, 2, 4.6);
        graphdDijkstra.addEdge(1, 2, 2.0);
        graphdDijkstra.addEdge(1, 3, 3.0);
        graphdDijkstra.addEdge(2, 3, 1.0);
        graphdDijkstra.addEdge(2, 4, 15.0);
        graphdDijkstra.addEdge(3, 4, 1.5);

        UndirectedGraph.Dijkstra dijkstra = graphdDijkstra.new Dijkstra(graphdDijkstra.getVertices());

        for (UndirectedGraph.Edge edge : graphdDijkstra.edges()) {
            dijkstra.addEdge(edge.start, edge.end, edge.weight);
        }
        double[] distances = dijkstra.shortestPath(0);

        System.out.println("Shortest paths from vertex " + 0 + " to all other connected vertices:");
        for (int i = 0; i < graphdDijkstra.getVertices(); i++) {
            if (i != 0) {
                System.out.println("Vertex " + i + ": distance = " + distances[i]);
            }
            else {
                System.out.println("Starting Vertex " + i + ": distance = " + distances[i]);
            }
        }

        System.out.println("\nBellman-Ford Algorithm:");

        DirectedGraph graphBellmanFord = new DirectedGraph(5);

        graphBellmanFord.addEdge(0, 1, 1.0);
        graphBellmanFord.addEdge(0, 2, -1.0);
        graphBellmanFord.addEdge(1, 2, 2.0);
        graphBellmanFord.addEdge(1, 3, 3.0);
        graphBellmanFord.addEdge(2, 3, 1.0);
        graphBellmanFord.addEdge(2, 4, 15.0);

        double[] dist = graphBellmanFord.bellmanFord(0);
        graphBellmanFord.displaybellmanFord(dist, 0);

        testDijkstraAndBellmanFord();

        System.out.println("\nProblem 5");
        System.out.println("Courses prerequisites: ");

        String[][] data = ReadData.readData("data/data.txt");
        CourseSchedule courses = new CourseSchedule(data);

        courses.display();
    }

    public static void testDijkstraAndBellmanFord() {
        System.out.println("Testing between Dijkstra and Bellman-Ford");
        Timer timer = new Timer();
        double timeDijkstra = 0.0;
        double timeBellmanFord = 0.0;
        int dijkstraCounter = 0;
        int bellmanFordCounter = 0;

        for (int i = 1_000; i <= 10_000; i += 1_000) {
            UndirectedGraph testDijkstra = new UndirectedGraph(i);
            DirectedGraph testBellmanFord = new DirectedGraph(i);
            UndirectedGraph.Dijkstra testdijkstra = testDijkstra.new Dijkstra(testDijkstra.getVertices());

            for (double j = 0.0; j < 2 * i; j++) {
                Random random = new Random();
                double w = random.nextDouble() * (2 * i);

                testDijkstra.addEdge(random.nextInt(i), random.nextInt(i), w);
                testBellmanFord.addEdge(random.nextInt(i), random.nextInt(i), w);
            }

            for (UndirectedGraph.Edge edge : testDijkstra.edges()) {
                testdijkstra.addEdge(edge.start, edge.end, edge.weight);
            }

            timer.Start();
            testdijkstra.shortestPath(0);
            timer.Stop();
            timeDijkstra += timer.getMilliSecond();
            timer.RestartTimer();

            timer.Start();
            testBellmanFord.bellmanFord(0);
            timer.Stop();
            timeBellmanFord += timer.getMilliSecond();
            timer.RestartTimer();

            if (timeDijkstra <= timeBellmanFord) {
                dijkstraCounter++;
            }
            else {
                bellmanFordCounter++;
            }

            //timedAlgorithms(timeDijkstra, timeBellmanFord);
            timeDijkstra = 0.0;
            timeBellmanFord = 0.0;
        }
        System.out.println("Dijkstra was faster " + dijkstraCounter + " times");
        System.out.println("Bellman Ford was faster " + bellmanFordCounter + " times");
    }

    public static void whatTime(double timeDijkstra, double timeBellmanFord) {
        System.out.println("Dijkstra took " + timeDijkstra + " ms");
        System.out.println("Bellman Ford took " + timeBellmanFord + " ms");
    }
    
}
