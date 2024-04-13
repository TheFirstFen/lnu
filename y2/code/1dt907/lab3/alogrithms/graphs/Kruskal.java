package alogrithms.graphs;

import java.util.ArrayList;
import java.util.List;

import alogrithms.Heap;
import alogrithms.PCWQUnionFind;

public class Kruskal<T> {
    private List<List<Edge<T>>> msf;
    private List<Double> weights;

    public Kruskal() {
        msf = new ArrayList<>();
        weights = new ArrayList<>();
    }

    public void runKruskal(UndirectedGraph<T> graph) {
        msf.clear();
        weights.clear();

        // * Unsorted edges
        List<Edge<T>> edges = new ArrayList<>();
        for (Edge<T> edge : graph.edges()) {
            edges.add(edge);
        }

        // * Into a min-heap
        Heap<T> heap = new Heap<T>(edges.size());
        for (Edge<T> edge : edges) {
            heap.push(edge);
        }

        // * Reset edges, and add sorted edges
        edges = new ArrayList<>();
        while (!heap.isEmpty()) {
            edges.add(heap.pop());
        }

        PCWQUnionFind uf = new PCWQUnionFind(graph.getVertices());

        for (Edge<T> edge : edges) {
            int v1 = (int) edge.v1;
            int v2 = (int) edge.v2;

            if (!uf.connected(v1, v2)) {
                uf.union(v1, v2);
            } else {
                continue;
            }

            List<Edge<T>> mstEdges = new ArrayList<>();
            mstEdges.add(edge);
            double weight = 0;

            for (List<Edge<T>> existingMST : msf) {
                if (existingMST.stream().anyMatch(e -> e.v1 == edge.v1 || e.v2 == edge.v1)) {
                    mstEdges.addAll(existingMST);
                    weights.remove(msf.indexOf(existingMST));
                    msf.remove(existingMST);
                    break;
                }
            }

            for (List<Edge<T>> existingMST : msf) {
                if (existingMST.stream().anyMatch(e -> e.v1 == edge.v2 || e.v2 == edge.v2)) {
                    mstEdges.addAll(existingMST);
                    weights.remove(msf.indexOf(existingMST));
                    msf.remove(existingMST);
                    break;
                }
            }

            msf.add(mstEdges);

            for (Edge<T> e : mstEdges) {
                weight += e.weight;
            }
            weights.add(weight);
        }
    }

    public void printMST() {
        System.out.println("Minimal spanning Forest:");
        for (int i = 0; i < msf.size(); i++) {
            System.out.println("Minimal spanning tree " + (i + 1) + " (weight: " + weights.get(i) + ")");
            System.out.println(msf.get(i) + "\n");
        }
    }
}
