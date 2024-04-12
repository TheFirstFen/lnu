import algorithms.queue.Person;
import algorithms.queue.TicketSys;

import java.util.Random;

public class Main3 {
    // TODO: Changes HeapSort for heapify.
    public static void main(String[] args) {
        TicketSys queue = new TicketSys();
        Random rnd = new Random();

        for (int i = 1; i < 2; i++) {
            queue = new TicketSys();

            for (int j = 0; j < 1_000_000 - 1; j++) {
                String id = String.valueOf(j);
                queue.insertPerson("test" + id, rnd.nextInt(10));
            }
            queue.insertPerson("Adam", 1);

            System.out.println("\nRunning tests for queue with: " + queue.getSize() + " persons");
            test(queue, rnd);
        }

        System.out.println("\nNext person to buy a ticket: " + queue.getPerson());

        queue.deleteMinPriority();
        System.out.println("Next person to buy a ticket after deleting: " + queue.getPerson());

        System.out.println("Next person to buy a ticket after swapping: " + queue.getPerson());

        queue.displayExample();
    }

    private static void test(TicketSys q, Random rnd) {
        Timer sw = new Timer();
        Person temp;

        System.out.print("Testing getPerson(): ");
        sw.start();
        temp = q.getPerson();
        sw.stop();
        System.out.println(sw.chooseTimePrefix(sw.getTimeInNanoSeconds()) + " (" + temp + ")");

        sw.reset();

        System.out.print("Testing insertPerson(): ");
        sw.start();
        q.insertPerson("Alice", 0);
        sw.stop();
        System.out.println(sw.chooseTimePrefix(sw.getTimeInNanoSeconds()) + " (Person{name='Alice', prio=0})");

        sw.reset();

        System.out.print("Testing swapPriority(): ");
        sw.start();
        q.swapPriority("Alice", "Adam");
        sw.stop();
        System.out.println(sw.chooseTimePrefix(sw.getTimeInNanoSeconds())
                + " (swaped Person{name='Alice', prio=0} & Person{name='Adam', prio=7})");

        sw.reset();

        System.out.print("Testing deleteMinPriority(): ");
        sw.start();
        temp = q.deleteMinPriority();
        sw.stop();
        System.out.println(sw.chooseTimePrefix(sw.getTimeInNanoSeconds()) + " (" + temp + ")");

        sw.reset();
    }
}
