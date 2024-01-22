import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import alogrithms.graphs.DirectedGraphString;
import alogrithms.graphs.EdgeString;

public class Main5 {
    public static void main(String[] args) {
        DirectedGraphString graph = readGraphFromFile("./data/data.txt");
        String startIdx = "START";

        List<String> stage1 = coursesWithNoPrerequisuites(graph);

        // * Needed ?
        for (String course : stage1) {
            addEdgeToGraph(graph, startIdx, course);
        }

        List<String> stage2 = coursesWithStage1AsPrerequisuites(graph, stage1);

        Iterable<String> courseOrder = DirectedGraphString.breadthFirstSearch(graph, startIdx);

        int stage = 1;
        int coursesInStage = 6;

        // * Debugging Versio
        // * Debuggingn
        for (String course : courseOrder) {
            if (course.equals(startIdx)) {
                continue;
            } else
                System.out.println("Stage " + stage + ": " + course);

            if (--coursesInStage == 0) {
                stage++;
                coursesInStage = getCoursesInStage(stage);
                System.out.println();
            }
        }
    }

    // * Debugging
    private static int getCoursesInStage(int stage) {
        switch (stage) {
            case 1:
                return 6;
            case 2:
                return 7;
            case 3:
                return 9;
            case 4:
                return 3;
            case 5:
                return 2;
            case 6:
                return 1;
            default:
                return 0;
        }
    }

    public static DirectedGraphString readGraphFromFile(String filePath) {
        DirectedGraphString graph = null;
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

    public static DirectedGraphString addEdgeToGraph(DirectedGraphString graph, String prerequisite, String course) {
        if (graph == null) {
            graph = new DirectedGraphString(50);
        }
        graph.addEdge(prerequisite, course);
        return graph;
    }

    private static List<String> coursesWithNoPrerequisuites(DirectedGraphString graph) {
        List<String> temp = new ArrayList<String>();
        for (String courseID : graph.vertices()) {
            for (EdgeString edge : graph.adjacent(courseID)) {
                temp.add(edge.v2);
            }
        }

        List<String> vertices = graph.verticesList();
        List<String> stage1 = new ArrayList<String>();
        for (String vertex : vertices) {
            if (!temp.contains(vertex)) {
                stage1.add(vertex);
            }
        }

        return stage1;
    }

    // * Testing, Not working
    private static List<String> coursesWithStage1AsPrerequisuites(DirectedGraphString graph, List<String> stage) {
        List<String> stage2 = new ArrayList<String>();
        List<String> temp = new ArrayList<String>();
        for (String courseID : stage) {
            for (EdgeString edge : graph.adjacent(courseID)) {
                temp.add(edge.v2);
            }
        }

        temp = temp.stream().distinct().toList(); // Removes duplicates

        for (String courseID : temp) {
            List<String> prerequisuite = new ArrayList<>();
            for (EdgeString edge : graph.adjacent(courseID)) {
                prerequisuite.add(edge.v1);
            }

            if (stage.containsAll(prerequisuite)) {
                stage2.add(courseID);
            }
        }

        return stage2;
    }
}
