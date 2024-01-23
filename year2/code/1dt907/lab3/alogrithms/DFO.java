package alogrithms;

import java.util.ArrayList;
import java.util.List;

import alogrithms.graphs.DirectedGraphString;
import alogrithms.graphs.Edge;

public class DFO<T> {
    public DFO(DirectedGraphString graph) {
        boolean[] visited = new boolean[graph.getVertices()];
        List<String> res = new ArrayList<>();

        for (int i = 0; i < graph.getVertices(); i++) {
            if (!visited[i]) {
                dfs(graph, i);
            }
        }
    }

    public void dfs(DirectedGraphString graph, int v) {
        visited[v] = true;
        for (Edge<T> edge : graph.adjacent(v)) {
            int neighborIndex = verticesList.indexOf(edge.v2);
            if (!visited[neighborIndex]) {
                dfs(neighborIndex, visited);
            }
        }

        path.add(verticesList.get(v));
    }
}
