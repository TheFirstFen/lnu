import alogrithms.graphs.Kruskal;
import alogrithms.graphs.UndirectedGraph;

import java.util.Random;

public class Main3 {
    public static void main(String[] args) {
        UndirectedGraph<Integer> graph = new UndirectedGraph<Integer>(15); // * 15 represent the largest vertex + 1
        Random rnd = new Random();

        graph.addEdge(0, 1, rnd.nextInt(1001) / 100.0);
        graph.addEdge(1, 2, rnd.nextInt(1001) / 100.0);
        graph.addEdge(1, 4, rnd.nextInt(1001) / 100.0);
        graph.addEdge(2, 3, rnd.nextInt(1001) / 100.0);
        graph.addEdge(2, 4, rnd.nextInt(1001) / 100.0);

        graph.addEdge(10, 11, rnd.nextInt(1001) / 100.0);
        graph.addEdge(10, 12, rnd.nextInt(1001) / 100.0);
        graph.addEdge(11, 12, rnd.nextInt(1001) / 100.0);
        graph.addEdge(11, 13, rnd.nextInt(1001) / 100.0);
        graph.addEdge(12, 14, rnd.nextInt(1001) / 100.0);

        Kruskal<Integer> kruskal = new Kruskal<Integer>();

        kruskal.runKruskal(graph);

        kruskal.printMST();
    }
}
