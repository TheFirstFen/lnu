package alogrithms.graphs;

class Graph {
    protected int vertices;
    protected int edges;

    public Graph(int vertices) {
        this.vertices = vertices;
        this.edges = 0;
    }

    public int getVertices() {
        return vertices;
    }

    public int getEdges() {
        return edges;
    }

    public void addEdge(int v, int w, double weight) {
        edges++;
    }

    public void removeEdge(int v, int w) {
        edges--;
    }

    public int degree(int v) {
        return 0;
    }

    public Iterable<Integer> vertices() {
        return null;
    }

    public Iterable<Edge> edges() {
        return null;
    }

    public Iterable<Edge> adjacent(int v) {
        return null;
    }
}