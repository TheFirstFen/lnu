package algorithms.queue;

public class Person implements Comparable<Person> {
    private String name;
    protected int prio;

    public Person(String name, int prio) {
        this.name = name;
        this.prio = prio;
    }

    public String getName() {
        return name;
    }

    public int getPriority() {
        return prio;
    }

    public void setPriority(int prio) {
        this.prio = prio;
    }

    @Override
    public int compareTo(Person other) {
        return Math.min(other.prio, this.prio);

    }

    @Override
    public String toString() {
        return "Person{name='" + name + "', prio=" + prio + '}';
    }
}
