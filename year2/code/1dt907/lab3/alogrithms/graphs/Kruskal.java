package alogrithms.graphs;

import alogrithms.*;

public class Kruskal {
    private Heap<Integer> heap;
    private PCWQUnionFind uf;

    public Kruskal(int heapCap, int vertices) {
        this.heap = new Heap<Integer>(heapCap);
        this.uf = new PCWQUnionFind(vertices);
    }

    public void addEdge(int v, int w, double weight) {
        Edge<Integer> edge = new Edge<Integer>(v, w, weight);
        Edge<Integer> rEdge = new Edge<Integer>(w, v, weight);
        heap.insert(edge);
        heap.insert(rEdge);
    }

    public void runKurskal() {
        while (!heap.isEmpty() && uf.getCount() > 1) {
            Edge<Integer> edge = heap.poll();
            int srcRoot = uf.find(edge.v1);
            int destRoot = uf.find(edge.v2);

            if (srcRoot != destRoot) {
                System.out.println("Edge: " + edge);
                uf.union(edge.v1, edge.v2);
            }
        }
    }
}
