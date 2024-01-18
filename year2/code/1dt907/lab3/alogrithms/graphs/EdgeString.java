package alogrithms.graphs;

public class EdgeString {
    public String v1;
    public String v2;
    public double weight;

    public EdgeString(String v1, String v2, double weight) {
        this.v1 = v1;
        this.v2 = v2;
        this.weight = weight;
    }

    @Override
    public String toString() {
        return "(" + v1 + " --> " + v2 + ") " + weight;
    }
}
