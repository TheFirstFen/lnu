package alogrithms.graphs;

class IGraph {
    protected int vertices;
    protected int edges;

    public IGraph(int vertices) {
        this.vertices = vertices;
        this.edges = 0;
    }

    public int getVertices() {
        return vertices;
    }

    public int getEdges() {
        return edges;
    }

    public void addEdge(int v, int w) {
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

    public Iterable<Integer> edges() {
        return null;
    }

    public Iterable<Integer> adjacent(int v) {
        return null;
    }
}