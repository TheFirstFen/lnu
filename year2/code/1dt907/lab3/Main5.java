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

        List<String> temp = new ArrayList<String>();
        // locate cousres without prerequisite
        for (String courseID : graph.vertices()) {
            for (EdgeString edge : graph.adjacent(courseID)) {
                temp.add(edge.v2);
            }
        }

        List<String> stage1 = new ArrayList<String>();
        List<String> vertices = graph.verticesList();
        for (String vertex : vertices) {
            if (!temp.contains(vertex)) {
                stage1.add(vertex);
            }
        }

        for (String course : stage1) {
            addEdgeToGraph(graph, startIdx, course);
        }

        Iterable<String> courseOrder = DirectedGraphString.breadthFirstSearch(graph, startIdx);

        int stage = 1;
        int coursesInStage = 6;

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
}
