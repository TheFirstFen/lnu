package algorithms.queue;

import java.util.Arrays;

public class TicketSys {
    private Person[] arr;
    protected int size;
    private static final int DEFAULT_CAP = 10;

    public TicketSys() {
        arr = new Person[DEFAULT_CAP];
        size = 0;
    }

    public void insertPerson(String name, int prio, int place) {
        if (size == arr.length) {
            resize();
        }

        arr[size] = new Person(name, prio, place);
        size++;
    }

    public Person getPerson() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }

        HeapSort.heapSort(arr, size);

        return arr[0];
    }

    public Person deleteMinPriority() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }

        HeapSort.heapSort(arr, size);

        Person temp = arr[0];

        arr[0] = arr[size - 1];
        arr[size - 1] = null;
        size--;

        HeapSort.heapSort(arr, size);

        return temp;
    }

    public void swapPriority(String name1, String name2) {
        int index1 = -1, index2 = -1;

        for (int i = 0; i < size; i++) {
            if (arr[i].getName().equals(name1)) {
                index1 = i;
            } else if (arr[i].getName().equals(name2)) {
                index2 = i;
            }
        }

        if (index1 == -1 || index2 == -1) {
            throw new IllegalArgumentException("Incorrect name");
        }

        int tempPrio = arr[index1].getPriority();
        arr[index1].setPriority(arr[index2].getPriority());
        arr[index2].setPriority(tempPrio);

        HeapSort.heapSort(arr, size);
    }

    private void resize() {
        int newCap = arr.length * 2;
        arr = Arrays.copyOf(arr, newCap);
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void firstTen() {
        for (int i = 0; i < 10; i++)
            System.out.println(i + ":" + arr[i]);
    }

    public int getSize() {
        return size;
    }
}

class HeapSort {
    public static void heapSort(Person[] arr, int size) {
        int n = size;

        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        for (int i = n - 1; i >= 0; i--) {
            swap(arr, 0, i);
            heapify(arr, i, 0);
        }
    }

    private static void heapify(Person[] arr, int n, int i) {
        int smallest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;

        if (l < n && arr[l].getPriority() > arr[smallest].getPriority()) {
            smallest = l;
        } else if (l < n && arr[l].getPriority() == arr[smallest].getPriority()) {
            if (arr[l].getPlace() > arr[smallest].getPlace()) {
                smallest = l;
            }
        }

        if (r < n && arr[r].getPriority() > arr[smallest].getPriority()) {
            smallest = r;
        } else if (r < n && arr[r].getPriority() == arr[smallest].getPriority()) {
            if (arr[r].getPlace() > arr[smallest].getPlace()) {
                smallest = r;
            }
        }

        if (smallest != i) {
            swap(arr, i, smallest);
            heapify(arr, n, smallest);
        }
    }

    private static void swap(Person[] arr, int i, int j) {
        Person temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

}