package Algoritmer;

import java.util.List;
import java.util.ArrayList;

public class CourseSchedule {
    protected List<String> vertices;
    protected List<List<CourseEdge>> adj;

    public CourseSchedule(String[][] data) {
        List<String> verticesSet = new ArrayList<>();
        for (String[] course : data) {
            if (!verticesSet.contains(course[0])) {
                verticesSet.add(course[0]);
            }
            if (!verticesSet.contains(course[1])) {
                verticesSet.add(course[1]);
            }
        }

        this.vertices = new ArrayList<>(verticesSet);

        this.adj = new ArrayList<>();
        for (int i = 0; i < this.vertices.size(); i++) {
            adj.add(new ArrayList<>());
        }

        for (String[] course : data) {
            addEdge(course[1], course[0]);
        }
    }

    private void addEdge(String start, String end) {
        int startIndex = vertices.indexOf(start);
        adj.get(startIndex).add(new CourseEdge(start, end));
    }

    public void display() {
        List<String> reverseOrder = new ArrayList<>();
        List<String> visited = new ArrayList<>();
        for (String course : vertices) {
            if (!visited.contains(course)) {
                dfs(course, visited, reverseOrder);
            }
        }

        for (int i = reverseOrder.size() - 1; i >= 0; i--) {
            System.out.println(reverseOrder.get(i));
        }
    }

    private void dfs(String course, List<String> visited, List<String> reverseOrder) {
        int index = vertices.indexOf(course);
        if (index == -1) return;

        visited.add(course);

        for (CourseEdge edge : adj.get(index)) {
            if (!visited.contains(edge.end)) {
                dfs(edge.end, visited, reverseOrder);
            }
        }

        reverseOrder.add(course);
    }

    public static void main(String[] args) {
        String[][] data = {{"0", "1"}, {"1", "2"}, {"2", "3"}, {"0", "3"}, {"4", "2"}};
        CourseSchedule schedule = new CourseSchedule(data);
        System.out.println("Course Schedule: ");
        schedule.display();
    }

    class CourseEdge {
        String start;
        String end;

        public CourseEdge(String start, String end) {
            this.start = start;
            this.end = end;
        }
    }
}