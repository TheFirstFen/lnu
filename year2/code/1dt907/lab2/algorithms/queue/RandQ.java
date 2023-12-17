package algorithms.queue;

import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.Random;

public class RandQ<Obj> implements Iterable<Obj> {
    private Obj[] queue;
    private int size;

    @SuppressWarnings("unchecked")
    public RandQ() {
        queue = (Obj[]) new Object[1];
        size = 0;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public int size() {
        return size;
    }

    public void enqueue(Obj obj) {
        if (obj == null) {
            throw new IllegalArgumentException("Cannot be null");
        }

        if (size == queue.length) {
            resize(2 * queue.length);
        }

        queue[size++] = obj;
    }

    public Obj dequeue() {
        if (isEmpty()) {
            throw new NoSuchElementException("Queue is empty");
        }

        int randomIndex = new Random().nextInt(size);
        Obj obj = queue[randomIndex];

        queue[randomIndex] = queue[size - 1];
        queue[size - 1] = null;
        size--;

        if (size > 0 && size == queue.length / 4) {
            resize(queue.length / 2);
        }

        return obj;
    }

    private void resize(int cap) {
        Obj[] temp = (Obj[]) java.util.Arrays.copyOf(queue, cap);

        for (int i = 0; i < size; i++) {
            temp[i] = queue[i];
        }

        queue = temp;
    }

    public Iterator<Obj> iterator() {
        return new RandQIterator();
    }

    private class RandQIterator implements Iterator<Obj> {

        private final Obj[] shuffledObj;
        private int curIdx;

        public RandQIterator() {
            shuffledObj = (Obj[]) java.util.Arrays.copyOf(queue, size);

            for (int i = 0; i < size; i++) {
                shuffledObj[i] = queue[i];
            }

            Random rnd = new Random();

            for (int i = size - 1; i > 0; i--) {
                int j = rnd.nextInt(i + 1);
                swap(shuffledObj, i, j);
            }

            curIdx = 0;
        }

        private void swap(Obj[] arr, int i, int j) {
            Obj temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }

        public boolean hasNext() {
            return curIdx < size;
        }

        public Obj next() {
            if (!hasNext()) {
                throw new NoSuchElementException("No more elements in queue");
            }

            return shuffledObj[curIdx++];
        }
    }
}
