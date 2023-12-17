import java.util.Random;

import algorithms.queue.RandQ;

public class Main1 {
    public static void main(String[] args) {
        RandQ<Integer> queue = new RandQ<>();
        Random rnd = new Random();

        System.out.println("Queue empty? " + queue.isEmpty());
        printQueue(queue);

        for (int i = 0; i < 10; i++) {
            queue.enqueue(rnd.nextInt(100));
        }

        System.out.println("Queue size: " + queue.size() + " elements");
        printQueue(queue);

        System.out.println("\nQueue empty? " + queue.isEmpty());

        System.out.println("\nDequeue: " + queue.dequeue());

        System.out.println("Queue size after dequeue: " + queue.size() + " elements");
        printQueue(queue);
    }

    public static void printQueue(RandQ<Integer> queue) {
        for (int i : queue) {
            System.out.print(i + " ");
        }
        System.out.println("");
    }
}
