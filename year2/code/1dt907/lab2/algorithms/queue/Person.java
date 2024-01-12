package algorithms.queue;

public class Person {
    private String name;
    protected int prio;
    protected int place;

    public Person(String name, int prio, int place) {
        this.name = name;
        this.prio = prio;
        this.place = place;
    }

    public String getName() {
        return name;
    }

    public int getPriority() {
        return prio;
    }

    public int getPlace() {
        return place;
    }

    public void setPriority(int prio) {
        this.prio = prio;
    }

    @Override
    public String toString() {
        return "Person{name='" + name + "', prio=" + prio + ", place=" + place + "}";
    }
}