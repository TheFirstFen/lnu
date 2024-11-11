package Assignment3;

import java.util.Arrays;


public class PQAsHeap {
    private HeapNode[] heap;
    private int size;
    private int startsize = 10;

    public PQAsHeap() {
        this.heap = new HeapNode[startsize];
        this.size = 0;
    }

    public void insert_person(String nam, double prio) {
        HeapNode person = new HeapNode(nam, prio);
        queueLengthChecker();
        heap[size] = person;
        size++;
        heapifyUp();
    }

    public HeapNode get_person() {
        if (size == 0) {
            throw new IllegalStateException("Empty heap!(getPerson)");
        }

        HeapNode root = heap[0];
        heap[0] = heap[size - 1];
        size--;
        heapifyDown();
        return root;
    }

    public void delete_max_prio() {
        if (size == 0) {
            throw new IllegalStateException("Empty heap!(maxprio)");
        }
    
        Double maxPriority = heap[0].getPrio();
        int lastIndex = size - 1;
    
        while (lastIndex >= 0 && heap[lastIndex].getPrio() == maxPriority) {
            lastIndex--;
        }
    
        if (lastIndex < 0) {
            size = 0;
        } else {
            size = lastIndex + 1;
    
            for (int i = 0; i < size; i++) {
                if (heap[i].getPrio() == maxPriority) {
                    heap[i] = heap[size - 1];
                    size--;
                    i--;
                }
            }
    
            heapifyDown();
        }
    }
    
    
    public void swap_priority(String name1, String name2) {
        int index1 = -1;
        int index2 = -1;
    
        for (int i = 0; i < size; i++) {
            if (heap[i].getName().equals(name1)) {
                index1 = i;
            } else if (heap[i].getName().equals(name2)) {
                index2 = i;
            }
        }
    
        if (index1 == -1 || index2 == -1) {
            throw new IllegalArgumentException("One or both names not found in the heap");
        }
    
        Double tempPriority = heap[index1].getPrio();
        heap[index1] = new HeapNode(name1, heap[index2].getPrio());
        heap[index2] = new HeapNode(name2, tempPriority);
    
        if (index1 < index2) {
            heapifyUp();
        } else {
            heapifyDown();
        }
    }
    
    private void heapifyUp() {
        int index = size - 1;
        while (index > 0) {
            int parentIndex = (index - 1) / 2;
            if (heap[index].getPrio() < heap[parentIndex].getPrio()) {
                swap(index, parentIndex);
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    private void heapifyDown() {
        int index = 0;
        while (true) {
            int leftChildIndex = 2 * index + 1;
            int rightChildIndex = 2 * index + 2;
            int smallest = index;

            if (leftChildIndex < size && heap[leftChildIndex].getPrio() < heap[smallest].getPrio()) {
                smallest = leftChildIndex;
            }

            if (rightChildIndex < size && heap[rightChildIndex].getPrio() < heap[smallest].getPrio()) {
                smallest = rightChildIndex;
            }

            if (smallest != index) {
                swap(index, smallest);
                index = smallest;
            } else {
                break;
            }
        }
    }

    private void swap(int i, int j) {
        HeapNode temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }

    private void queueLengthChecker() {
        if (size == heap.length) {
            heap = Arrays.copyOf(heap, 2 * heap.length);
        }
    }
    public Boolean isEmpty() {
        if (size == 0) {
            return true;
        } else {
            return false;
        }
    }


}
