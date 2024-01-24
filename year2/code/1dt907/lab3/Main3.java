import java.util.ArrayList;
import java.util.List;

import alogrithms.graphs.Kruskal;
import alogrithms.graphs.Edge;

public class Main3 {
    public static void main(String[] args) {
        List<Edge<Integer>> edges = new ArrayList<>();

        edges.add(new Edge<Integer>(0, 2, 3.2));
        edges.add(new Edge<Integer>(1, 2, 1.2));
        edges.add(new Edge<Integer>(2, 3, 4.3));
        edges.add(new Edge<Integer>(3, 4, 2.2));

        edges.add(new Edge<Integer>(5, 6, 2.5));
        edges.add(new Edge<Integer>(7, 6, 1.8));
        edges.add(new Edge<Integer>(6, 8, 3.2));
        edges.add(new Edge<Integer>(8, 9, 1.5));

        Kruskal<Integer> kruskal = new Kruskal<Integer>();

        for (List<Edge<Integer>> tree : kruskal.runKurskal(edges, edges.size() * 2)) {
            System.out.println("Tree:");
            for (Edge<Integer> edge : tree) {
                System.out.println(edge);
            }
        }

        // kruskal.addEdge(0, 2, 3.2);
        // kruskal.addEdge(1, 2, 1.2);
        // kruskal.addEdge(2, 3, 4.3);
        // kruskal.addEdge(3, 4, 2.2);

    }
}
