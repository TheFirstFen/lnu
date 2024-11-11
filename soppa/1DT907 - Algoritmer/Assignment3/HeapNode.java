package Assignment3;

public class HeapNode {
    private String name;
    private Double priority;

    public HeapNode(String nam, Double prio) {
        name = nam;
        priority = prio;
    }

    public String getName() {
        return name;
    }
    public Double getPrio() {
        return priority;
    }
}
