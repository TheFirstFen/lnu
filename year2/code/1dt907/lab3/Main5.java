import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import alogrithms.graphs.DirectedGraph;
import alogrithms.graphs.Edge;

public class Main5 {
    public static void main(String[] args) {
        DirectedGraph<String> graph = readGraphFromFile("./data/data.txt");

        graph.vertices();
        // graph.topologicalSort();
    }

    public static DirectedGraph<String> readGraphFromFile(String filePath) {
        DirectedGraph<String> graph = null;
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] courses = line.split(";");
                graph = addEdgeToGraph(graph, courses[1], courses[0]);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return graph;
    }

    public static DirectedGraph<String> addEdgeToGraph(DirectedGraph<String> graph, String prerequisite,
            String course) {
        if (graph == null) {
            graph = new DirectedGraph<String>(0);
        }
        graph.addEdge(prerequisite, course);
        return graph;
    }
}
