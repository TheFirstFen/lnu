import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import alogrithms.graphs.DirectedGraph;
import alogrithms.DFO;

public class Main5 {
    protected static List<String> uniqueCourses = new ArrayList<>();

    public static void main(String[] args) {
        DirectedGraph<String> graph = readGraphFromFile("./data/data.txt");

        DFO dfo = new DFO(graph);
        for (String s : dfo.reverse_res()) {
            System.out.println(s);
        }
    }

    public static DirectedGraph<String> readGraphFromFile(String filePath) {
        DirectedGraph<String> graph = null;

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] courses = line.split(";");
                if (!uniqueCourses.contains(courses[0])) {
                    uniqueCourses.add(courses[0]);
                }
                if (!uniqueCourses.contains(courses[1])) {
                    uniqueCourses.add(courses[1]);
                }
            }

            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] courses = line.split(";");
                graph = addEdgeToGraph(graph, courses[1], courses[0]);
            }

            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return graph;
    }

    public static DirectedGraph<String> addEdgeToGraph(DirectedGraph<String> graph, String prerequisite,
            String course) {
        if (graph == null) {
            graph = new DirectedGraph<String>(uniqueCourses.size()); // numVertices
        }
        graph.addEdge(prerequisite, course);
        return graph;
    }
}
