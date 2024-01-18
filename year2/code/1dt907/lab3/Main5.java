import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import alogrithms.graphs.DirectedGraphString;

public class Main5 {
    public static void main(String[] args) {
        DirectedGraphString graph = readGraphFromFile("./data/data.txt");
        Iterable<String> courseOrder = DirectedGraphString.topologicalSort(graph);

        System.out.println("Course order to fulfill prerequisites:");
        for (String course : courseOrder) {
            System.out.println(course);
        }
    }

    public static DirectedGraphString readGraphFromFile(String filePath) {
        DirectedGraphString graph = null;
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] courses = line.split(";");
                graph = addEdgeToGraph(graph, courses[0], courses[1]);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return graph;
    }

    public static DirectedGraphString addEdgeToGraph(DirectedGraphString graph, String course, String prerequisite) {
        if (graph == null) {
            graph = new DirectedGraphString(30);
        }
        graph.addEdge(course, prerequisite);
        return graph;
    }
}
