package algorithms.queue;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class PriorityQ {
    private static Map<String, Integer> pMap;

    private final PriorityQueue<Person> queue;

    public PriorityQ() {
        pMap = new HashMap<>();
        queue = new PriorityQueue<>();
    }

    private static class Person implements Comparable<Person> {
        String name;
        int prio;

        public Person(String name, int prio) {
            this.name = name;
            this.prio = prio;
        }

        @Override
        public int compareTo(Person other) {
            if (this.prio != other.prio) {
                return Integer.compare(other.prio, this.prio);
            }

            return Integer.compare(pMap.get(this.name), pMap.get(other.name));
        }
    }

    public void insertPerson(String name, int prio) {
        Person person = new Person(name, prio);
        pMap.put(name, prio);
        queue.add(person);
    }

    public String getPerson() {
        return queue.peek().name;
    }

    public void deleteMaxPriority() {
        Person removedPerson = queue.poll();
        pMap.remove(removedPerson.name);
    }

    public void swapPriority(String name1, String name2) {
        int priority1 = pMap.get(name1);
        int priority2 = pMap.get(name2);

        pMap.put(name1, priority2);
        pMap.put(name2, priority1);

        queue.clear();

        for (Map.Entry<String, Integer> entry : pMap.entrySet()) {
            queue.add(new Person(entry.getKey(), entry.getValue()));
        }
    }
}
