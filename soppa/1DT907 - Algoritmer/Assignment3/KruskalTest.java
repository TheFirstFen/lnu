package Assignment3;

import java.util.List;

import Assignment3.Graph.Edge;

public class KruskalTest {
    public static void main(String[] args) {
        testUndirectedGraph();
    }

    private static void testUndirectedGraph() {
        UndirectedGraph undirectedGraph = new UndirectedGraph();
        undirectedGraph.addVertex(1);
        undirectedGraph.addVertex(2);
        undirectedGraph.addVertex(3);
        undirectedGraph.addVertex(4);
        undirectedGraph.addVertex(5);
        undirectedGraph.addVertex(6);
        undirectedGraph.addVertex(7);
        undirectedGraph.addVertex(8);
        undirectedGraph.addVertex(9);
        undirectedGraph.addEdgeWithWeight(2, 4, 1.0);
        undirectedGraph.addEdgeWithWeight(2, 1, 1.0);
        undirectedGraph.addEdgeWithWeight(2,3, 2.0);
        undirectedGraph.addEdgeWithWeight(3, 5, 2.0);
        undirectedGraph.addEdgeWithWeight(5, 6, 3.0);
        undirectedGraph.addEdgeWithWeight(6, 7, 3.0);
        undirectedGraph.addEdgeWithWeight(8, 9, 3.0);


        System.out.println("Original Graph:");
        undirectedGraph.printGraph();

        Iterable<List<Edge>> minimalSpanningForest = undirectedGraph.kruskal();

        System.out.println("\nMinimal Spanning Forest:");
        printEdges(minimalSpanningForest);
    }

    private static void printEdges(Iterable<List<Edge>> minimalSpanningForest) {
        int i = 1;
        for (List<Edge> mst : minimalSpanningForest) {
            System.out.println("Tree " + i + " - " + mst);
            i ++;
        }
    }
}
