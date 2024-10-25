package Algorithm;

import java.util.Random;
import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.Arrays;

// implements Iterator<Obj>
public class RandomQueue <Obj> implements Iterable<Obj> {
    private Object[] queue;
    private int size;
    private static final Random random = new Random();

    public RandomQueue() {
        queue = new Object[10];
        size = 0;
    }
    
    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void enqueue(Obj element) {
        if (size == queue.length) {
            resize(2* queue.length);
        }
        queue[size++] = element;
    }

    public Object dequeue() {
        if (isEmpty()) {
            throw new NoSuchElementException("No elements in the queue");
        }
        int randomIndex = random.nextInt(size);
        Object removedElement = queue[randomIndex];

        queue[randomIndex] = queue[size - 1];
        queue[size - 1] = null;

        size--;

        if (size > 0 && size == queue.length / 4) {
            resize(queue.length / 2);
        }

        return removedElement;
    }


    private void resize(int capacity) {
        Object[] newArray = new Object[capacity];
        System.arraycopy(queue, 0, newArray, 0, size);
        queue = newArray;
    }

    public static void printQueue(RandomQueue<Integer> randomQueue) {
        for (int element : randomQueue) {
            System.out.print(element + " ");
        }
        System.out.println();
    }

    private class RandomQueueIterator implements Iterator<Obj> {
        private int currentIndex;
        private final Object[] randomObjects;

        public RandomQueueIterator() {
            randomObjects = Arrays.copyOf(queue, size);

            for (int i = 0; i < size; i++) {
                randomObjects[i] = queue[i];
            }

            Random random = new Random();
            
            for (int i = size - 1; i > 0; i--) {
                int randomIndex = random.nextInt(i + 1);
                swap(randomObjects, i, randomIndex);
            }
            currentIndex = 0;
        }

        private void swap(Object[] array, int i, int j) {
            Object temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }

        @Override
        public boolean hasNext() {
            return currentIndex < size;
        }

        @Override 
        public Obj next() {
            if (!hasNext()) {
                throw new NoSuchElementException("No moew elemnts in the queue");
            }
            return (Obj) randomObjects[currentIndex++];
        }
    }

    public Iterator<Obj> iterator() {
        return new RandomQueueIterator();
    }

    public static void main(String[] args) {
        RandomQueue<Integer> randomQueue = new RandomQueue<>();

        randomQueue.enqueue(1);
        randomQueue.enqueue(2);
        randomQueue.enqueue(3);
        randomQueue.enqueue(4);

        System.out.println("Size: " + randomQueue.size());
        System.out.println("Is Empty: " + randomQueue.isEmpty());

        System.out.println("Dequeued: " + randomQueue.dequeue());

        System.out.println("Size: " + randomQueue.size());
        System.out.println("Is Empty: " + randomQueue.isEmpty());
    }
}
