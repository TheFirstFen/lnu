package Algorithm;

import java.util.Arrays;
import java.util.Random;

public class Ticket {
    class Person {
        String name;
        int priority;
        int time;

        public Person(String name, int priority, int time) {
            this.name = name;
            this.priority = priority;
            this.time = time;
        }
    }

    private Person[] queue;
    private int size;

    public Ticket() {
        queue = new Person[10];
        size = 0;
    }

    private void resizeQueue() {
        queue = Arrays.copyOf(queue, size * 2);
    }

    public void insertPerson(String name, int priority, int time) {
        if (size == queue.length) {
            resizeQueue();
        }

        Person person = new Person(name, priority, time);
        queue[size++] = person;
    }

    public Person getPerson() {
        heapSort();
        return queue[0];
    }

    public void deleteMaxPriority() {
        if (size > 0) {
            heapSort();
            swap(0, size-1);
            size--;
            heapSort();
        }
        else {
            System.out.println("Queue is empty.");
        }
    }

    public void swap(int index1, int index2) {
        Person temp = queue[index1];
        queue[index1] = queue[index2];
        queue[index2] = temp;
    }

    private void heapSort() {
        
        for (int i = size / 2 - 1; i >= 0; i--) {
            heapify(size, i);
        }

        for (int i = size - 1; i >= 0; i--) {
            swap(0, i);
            heapify(i, 0);
        }
    }

    private void heapify(int n, int index) {
        int l = 2 * index + 1;
        int r = 2 * index + 2;
        int s = index;

        if (l < n && queue[l].priority > queue[s].priority) {
            s = l;
        }
        else if (l < n && queue[l].priority == queue[s].priority) {
            if (queue[l].time > queue[s].time) {
                s = l;
            }
        }

        if (r < n && queue[r].priority > queue[s].priority) {
            s = r;
        }
        else if (r < n && queue[r].priority == queue[s].priority) {
            if (queue[r].time > queue[s].time) {
                s = r;
            }
        }

        if (s != index) {
            swap(index, s);
            heapify(n, s);
        }
    }

    public void swapPriority(String name1, String name2) {
        int index1 = -1;
        int index2 = -1;
        for (int i = 0; i < size; i++) {
            if (queue[i].name.equals(name1)) {
                index1 = i;
            } else if (queue[i].name.equals(name2)) {
                index2 = i;
            }
        }

        if (index1 != -1 && index2 != -1) {
            int temp = queue[index1].priority;
            queue[index1].priority = queue[index2].priority;
            queue[index2].priority = temp;  
            
        }
        heapSort();
    }

    public void displayQueue() {
        System.out.println("Queue:");
        for (int i = 0; i < size; i++) {
            Person person = queue[i];
            System.out.println("Name: " + person.name + ", Priority: " + person.priority + ", Time: " + person.time);
        }
    }

    public void printfirst10queue() {
        System.out.println("First 10 in the Queue:");
        for (int i = 0; i < 10; i++) {
            Person person = queue[i];
            System.out.println("Name: " + person.name + ", Priority: " + person.priority + ", Time: " + person.time);
        }
    }

    public static void main(String[] args) {
        Ticket ticketSystem = new Ticket();
        Random Random = new Random();
        for (int i = 0; i < 20; i++) {
            int b = Random.nextInt(0, 5);
            ticketSystem.insertPerson("Person" + i, b, i);
        }
        ticketSystem.displayQueue();

        System.out.println("Next person to buy a ticket: " + ticketSystem.getPerson().name);

        System.out.println("After getPerson:");
        ticketSystem.displayQueue();

        System.out.println("swaping person 1 and 3");

        ticketSystem.swapPriority("Person1", "Person3");
        ticketSystem.displayQueue();

        System.out.println("Next person to buy a ticket after swapping: " + ticketSystem.getPerson().name);
        ticketSystem.displayQueue();

        System.out.println("Deleting max priority");
        ticketSystem.deleteMaxPriority();
        ticketSystem.displayQueue();

        System.out.println("Next person to buy a ticket: " + ticketSystem.getPerson().name);

        ticketSystem.displayQueue();
    }
}