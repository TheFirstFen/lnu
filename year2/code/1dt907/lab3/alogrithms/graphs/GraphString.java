package alogrithms.graphs;

import java.util.ArrayList;
import java.util.List;

public abstract class GraphString<T> {
    protected int vertices;
    protected List<T> verticesList;
    protected int edges;

    public GraphString(int vertices) {
        this.vertices = vertices;
        this.verticesList = new ArrayList<>(vertices);
        this.edges = 0;
    }

    public int getVertices() {
        return vertices;
    }

    public int getEdges() {
        return edges;
    }

    public void addEdge(T v, T w) {
        addEdge(v, w, 1.0);
    }

    public void addEdge(T v, T w, double weight) {
        if (!verticesList.contains(v)) {
            verticesList.add(v);
        }
        if (!verticesList.contains(w)) {
            verticesList.add(w);
        }
        edges++;
    }

    public void removeEdge(T v, T w) {
        edges--;
    }

    public int degree(T v) {
        return 0;
    }

    public Iterable<T> vertices() {
        return verticesList;
    }

    public Iterable<EdgeString> edges() {
        return null;
    }

    public Iterable<EdgeString> adjacent(T v) {
        return null;
    }
}
