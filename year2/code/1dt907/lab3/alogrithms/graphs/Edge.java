package alogrithms.graphs;

public class Edge {
    public int v1;
    public int v2;
    public double weight;

    public Edge(int v1, int v2, double weight) {
        this.v1 = v1;
        this.v2 = v2;
        this.weight = weight;
    }

    @Override
    public String toString() {
        return "(" + v1 + " - " + v2 + ", " + weight + ")";
    }
}
