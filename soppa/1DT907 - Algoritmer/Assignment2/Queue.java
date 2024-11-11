package Assignment2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class Queue {
    private int[] qArray;
    private int size;
    private int front;
    private int back;
    
    public Queue() {
        qArray = new int[10];
        size = 10;
        front = 0;
        back = 0;
    }

    public void enqueue(int v) {
        if (back < size) {
            qArray[back] = v;
            back += 1;
        } else {
            int[] tempArray = qArray;
            qArray = new int[size * 2];
            size = size * 2;
            int i = 0;
            while (i < back) {
                qArray[i] = tempArray[i];
                i ++;
            }
            qArray[back] = v;
            back += 1;
        }
    }

    public int dequeue() {
        if (front < size || front < back) {
            Random random = new Random();
            int randIndex = front + random.nextInt(back - front);
            int removeValue = qArray[randIndex];
            qArray[randIndex] = qArray[back - 1];
            qArray[back - 1] = removeValue;
            back --;
            if (count() < (size / 2) + 1 && size > 10) {
                int[] tempArray = qArray;
                qArray = new int[size / 2];
                size = size / 2;
                int i = 0;
                while (i < back) {
                    qArray[i] = tempArray[i];
                    i ++;
                }
            }
            return removeValue;
        } else {
            throw new IllegalStateException("Queue is empty!");
        }
    }

    public int count() {
        return back - front;
    }

    public boolean empty() {
        return back == front;
    }

    private class randQueueIterator {
        private List<Integer> shuffledQ;
        private int indexCount;


        public randQueueIterator(Queue q) {
            shuffledQ = new ArrayList<>();
            indexCount = 0;

            for (int i = q.front; i < q.back; i++) {
                shuffledQ.add(q.qArray[i]);
            }
            Collections.shuffle(shuffledQ);
        }

        private boolean hasNext() {
            return indexCount < shuffledQ.size();
        }

        public Integer getNext() {
            if (!hasNext()) {
                throw new IllegalStateException("No elements left!");
            }
            Integer tempValue = shuffledQ.get(indexCount);
            indexCount ++;
            return tempValue;
        }
    }

    public static void main(String[] args) {
        Queue q = new Queue();
        System.out.println(q.empty()); // Should return true
        for (int n = 1; n < 13; n ++) {
            q.enqueue(n);
        }
        System.out.println(q.size); // The size should be doubled to 20
        
        q.dequeue();

        System.out.println(q.size); // Should still be 20

        q.dequeue();

        System.out.println(q.empty()); // Should be false
        System.out.println(q.count()); // Should be 10
        
        
        System.out.println(q.size); // Should halved the size to 10 again
        
        // Here we print all values in random order using the iterator
        System.out.println("Heres all queue values in random order:");
        randQueueIterator iter = q.new randQueueIterator(q);
        while (iter.hasNext()) {
            System.out.print(iter.getNext() + ", ");
        }
    }
}
