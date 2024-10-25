package alogrithms.graphs;

public class EdgeDirected<T> implements Comparable<EdgeDirected<T>> {
    public T v1;
    public T v2;
    public double weight;

    public EdgeDirected(T v1, T v2, double weight) {
        this.v1 = v1;
        this.v2 = v2;
        this.weight = weight;
    }

    @Override
    public int compareTo(EdgeDirected<T> other) {
        if (this.weight < other.weight) {
            return -1;
        } else if (this.weight > other.weight) {
            return 1;
        } else {
            return 0;
        }
    }

    @Override
    public String toString() {
        return "(" + v1 + " -> " + v2 + ", " + weight + ")";
    }
}
