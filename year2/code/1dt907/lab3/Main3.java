import alogrithms.graphs.Kruskal;

public class Main3 {
    public static void main(String[] args) {
        Kruskal kruskal = new Kruskal(6, 6);

        kruskal.addEdge(0, 2, 3.2);
        kruskal.addEdge(1, 2, 1.2);
        kruskal.addEdge(2, 3, 4.3);
        kruskal.addEdge(3, 4, 2.2);

        kruskal.runKurskal();
    }
}
