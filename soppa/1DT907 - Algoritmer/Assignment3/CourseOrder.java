package Assignment3;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;


public class CourseOrder {
    private static Map<Integer, String> courseMap;

    public List<Integer> courseOrder(String[] courses) {
        DirectedGraph graph = buildGraph(courses);
        List<Integer> order = dfs(graph);
        return order;
    }

    private List<Integer> dfs(DirectedGraph graph) {
        List<Integer> order = new ArrayList<>();
        Set<Integer> visited = new HashSet<>();

        for (int vertex : graph.vertices()) {
            if (!visited.contains(vertex)) {
                dfsHelper(vertex, visited, order, graph);
            }
        }

        Collections.reverse(order);
        return order;
    }

    private void dfsHelper(int vertex, Set<Integer> visited, List<Integer> order, DirectedGraph graph) {
        visited.add(vertex);
        for (Graph.Edge edge : graph.adjacency(vertex)) {
            int neighbor = edge.getDestination();
            if (!visited.contains(neighbor)) {
                dfsHelper(neighbor, visited, order, graph);
            }
        }
        order.add(vertex);
    }

    private DirectedGraph buildGraph(String[] courses) {
        DirectedGraph graph = new DirectedGraph();
        courseMap = new HashMap<>();
        int count = 0;
        for (String course : courses) {
            String[] parts = course.split(";");
            String courseVertex = parts[0];
            String prereqVertex = parts[1];
            // Use a map to connect integers to all courses so i can use my implementation of graph
            if (!courseMap.containsValue(courseVertex)) {
                courseMap.put(count, courseVertex);
                graph.addVertex(count);
                count++;
            }
            if (!courseMap.containsValue(prereqVertex)) {
                courseMap.put(count, prereqVertex);
                graph.addVertex(count);
                count++;
            }
            graph.addEdgeWithWeight(getKeyFromValue(courseMap, prereqVertex), getKeyFromValue(courseMap, courseVertex), 0);
        }
        return graph;
    }

    private static <K, V> K getKeyFromValue(Map<K, V> map, V value) {
        for (Map.Entry<K, V> entry : map.entrySet()) {
            if (Objects.equals(value, entry.getValue())) {
                return entry.getKey();
            }
        }
        return null;
    }

    public static void main(String[] args) {
        String fileName = "Assignment3/data.txt";
        List<String> courseList = readCoursesFromFile(fileName);

        CourseOrder scheduler = new CourseOrder();
        List<Integer> order = scheduler.courseOrder(courseList.toArray(new String[0]));
        System.out.println("Course order:");
        for (int course : order) {
            System.out.println(courseMap.get(course));
        }
    }

    private static List<String> readCoursesFromFile(String fileName) {
        List<String> courseList = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                courseList.add(line);
            }
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
        return courseList;
    }
}
