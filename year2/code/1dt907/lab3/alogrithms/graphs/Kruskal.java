package alogrithms.graphs;

import alogrithms.*;

public class Kruskal {
    private Heap heap;
    private PCWQUnionFind uf;

    public Kruskal(int heapCap, int vertices) {
        this.heap = new Heap(heapCap);
        this.uf = new PCWQUnionFind(vertices);
    }

    public void addEdge(int v, int w, double weight) {
        Edge edge = new Edge(v, w, weight);
        heap.insert(edge);
    }

    public void runKurskal() {
        while (!heap.isEmpty() && uf.getCount() > 1) {
            Edge edge = heap.poll();
            int srcRoot = uf.find(edge.v1);
            int destRoot = uf.find(edge.v2);

            if (srcRoot != destRoot) {
                System.out.println("Edge: " + edge);
                uf.union(edge.v1, edge.v2);
            }
        }
    }
}
