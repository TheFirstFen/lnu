import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import alogrithms.graphs.DirectedGraphString;

public class Main5 {
    public static void main(String[] args) {
        DirectedGraphString graph = readGraphFromFile("./data/data.txt");
        Iterable<String> courseOrder = DirectedGraphString.topologicalSort(graph);

        int stage = 1;
        int coursesInStage = 6;

        for (String course : courseOrder) {
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
                graph = addEdgeToGraph(graph, courses[0], courses[1]);
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
