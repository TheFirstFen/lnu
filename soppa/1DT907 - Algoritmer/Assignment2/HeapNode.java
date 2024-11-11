package Assignment2;

public class HeapNode {
    private String name;
    private int priority;

    public HeapNode(String nam, int prio) {
        name = nam;
        priority = prio;
    }

    public String getName() {
        return name;
    }
    public int getPrio() {
        return priority;
    }
}
