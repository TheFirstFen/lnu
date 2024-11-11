package Assignment3;

public class GraphTraversalTest {
    public static void main(String[] args) {
        testUndirectedGraph();
        testDirectedGraph();
    }

    private static void testUndirectedGraph() {
        System.out.println("Testing Undirected Graph:");

        UndirectedGraph undirectedGraph = new UndirectedGraph();
        undirectedGraph.addVertex(1);
        undirectedGraph.addVertex(2);
        undirectedGraph.addVertex(3);
        undirectedGraph.addVertex(4);
        undirectedGraph.addEdge(1, 2);
        undirectedGraph.addEdge(2, 3);
        undirectedGraph.addEdge(3, 4);
        undirectedGraph.addEdge(4, 1);

        System.out.println("DFS traversal starting from vertex 1: " + traversalToString(undirectedGraph.dfs(1)));
        System.out.println("BFS traversal starting from vertex 1: " + traversalToString(undirectedGraph.bfs(1)));
        System.out.println();
    }

    private static void testDirectedGraph() {
        System.out.println("Testing Directed Graph:");

        DirectedGraph directedGraph = new DirectedGraph();
        directedGraph.addVertex(1);
        directedGraph.addVertex(2);
        directedGraph.addVertex(3);
        directedGraph.addVertex(4);
        directedGraph.addEdgeDefaultWeight(1, 2);
        directedGraph.addEdgeDefaultWeight(2, 3);
        directedGraph.addEdgeDefaultWeight(3, 4);
        directedGraph.addEdgeDefaultWeight(4, 1);

        System.out.println("DFS traversal starting from vertex 1: " + traversalToString(directedGraph.dfs(1)));
        System.out.println("BFS traversal starting from vertex 1: " + traversalToString(directedGraph.bfs(1)));
        System.out.println();
    }

    private static String traversalToString(Iterable<Integer> traversal) {
        StringBuilder result = new StringBuilder();
        for (int vertex : traversal) {
            result.append(vertex).append(" ");
        }
        return result.toString();
    }
}
