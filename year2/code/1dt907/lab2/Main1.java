import algorithms.queue.RandQ;

public class Main1 { // TODO: Make proper main.java
    public static void main(String[] args) {
        RandQ<Integer> queue = new RandQ<>();

        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        queue.enqueue(4);

        System.out.println("Randomized Queue: " + queue.size() + " elements");
        for (int obj : queue) {
            System.out.print(obj + " ");
        }

        System.out.println("\nDequeue: " + queue.dequeue());

        System.out.println("Randomized Queue after dequeue: " + queue.size() + " elements");

        for (int obj : queue) {
            System.out.print(obj + " ");
        }
    }
}
