import alogrithms.graphs.Kruskal;
import alogrithms.graphs.UndirectedGraph;

public class Main3 {
    public static void main(String[] args) {
        UndirectedGraph<Integer> graph = new UndirectedGraph<Integer>(15); // * 15 represent the largest v + 1

        graph.addEdge(0, 1, 1);
        graph.addEdge(1, 2, 2);
        graph.addEdge(1, 4, 100); // * Shouldn't be included in MST
        graph.addEdge(2, 3, 5);
        graph.addEdge(2, 4, 3);

        graph.addEdge(10, 11, 1);
        graph.addEdge(10, 12, 2);
        graph.addEdge(11, 12, 100);
        graph.addEdge(11, 13, 5);
        graph.addEdge(12, 14, 3);

        Kruskal<Integer> kruskal = new Kruskal<Integer>();

        kruskal.runKruskal(graph);

        kruskal.printMST();
    }
}
