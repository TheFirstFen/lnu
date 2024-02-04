package alogrithms;

import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

import alogrithms.graphs.DirectedGraph;
import alogrithms.graphs.EdgeDirected;

public class DFO {
    boolean[] visited;
    List<String> res;

    public DFO(DirectedGraph<String> graph) {
        visited = new boolean[graph.getVertices()];
        res = new ArrayList<>();
        for (int i = 0; i < graph.getVertices(); i++) {
            if (!visited[i]) {
                dfs(graph, i);
            }
        }
    }

    private void dfs(DirectedGraph<String> graph, int v) {
        visited[v] = true;
        for (EdgeDirected<String> edge : graph.adjacent(v)) {
            int nIdx = graph.verticesList().indexOf(edge.v2);
            if (!visited[nIdx]) {
                dfs(graph, nIdx);
            }
        }

        res.add(graph.verticesList().get(v));
    }

    public List<String> reverse_res() {
        Collections.reverse(res);
        return res;
    }
}
