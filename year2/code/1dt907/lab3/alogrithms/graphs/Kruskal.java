package alogrithms.graphs;

import java.util.ArrayList;
import java.util.List;

import alogrithms.*;

public class Kruskal<T> {
    // private Heap<Integer> heap;
    // private PCWQUnionFind uf;

    // public Kruskal(int heapCap, int vertices) {
    // this.heap = new Heap<Integer>(heapCap);
    // this.uf = new PCWQUnionFind(vertices);
    // }

    // public void addEdge(int v, int w, double weight) {
    // Edge<Integer> edge = new Edge<Integer>(v, w, weight);
    // Edge<Integer> rEdge = new Edge<Integer>(w, v, weight);
    // heap.insert(edge);
    // heap.insert(rEdge);
    // }

    // public void runKurskal() {
    // while (!heap.isEmpty() && uf.getCount() > 1) {
    // Edge<Integer> edge = heap.poll();
    // int srcRoot = uf.find(edge.v1);
    // int destRoot = uf.find(edge.v2);

    // if (srcRoot != destRoot) {
    // System.out.println("Edge: " + edge);
    // uf.union(edge.v1, edge.v2);
    // }
    // }
    // }

    public List<List<Edge<T>>> runKurskal(List<Edge<T>> edges, int numVertices) {
        Heap<T> minHeap = new Heap<>(numVertices);

        for (Edge<T> edge : edges) {
            minHeap.insert(edge);
        }

        PCWQUnionFind unionFind = new PCWQUnionFind(numVertices);

        List<List<Edge<T>>> minimalSpanningForest = new ArrayList<>();

        while (!minHeap.isEmpty() && minimalSpanningForest.size() < numVertices - 1) {
            Edge<T> edge = minHeap.poll();

            int root1 = unionFind.find((int) edge.v1);
            int root2 = unionFind.find((int) edge.v2);

            if (root1 != root2) {
                List<Edge<T>> newTree = new ArrayList<>();
                newTree.add(edge);
                minimalSpanningForest.add(newTree);

                unionFind.union(root1, root2);
            } else {
                for (List<Edge<T>> tree : minimalSpanningForest) {
                    if (unionFind.find((int) tree.get(0).v1) == root1) {
                        tree.add(edge);
                        break;
                    }
                }
            }
        }

        return minimalSpanningForest;
    }
}
