package algorithms.queue;

import java.util.Arrays;
import java.util.Comparator;

public class TicketSys {
    private Person[] arr;
    private int size;
    private static final int DEFAULT_CAP = 10;

    public TicketSys() {
        arr = new Person[DEFAULT_CAP];
        size = 0;
    }

    public void insertPerson(String name, int prio) {
        if (size == arr.length) {
            resize();
        }

        arr[size] = new Person(name, prio);
        size++;
        Quicksort.quickSort(arr, 0, size - 1);

        // * Att använda detta vart enda sättet jag hittade för att kunna hantera mer än
        // * 10 000 presoner i kön
        // Arrays.sort(arr, 0, size, Comparator.comparingInt(p -> p.prio));
    }

    public Person getPerson() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }

        return arr[0];
    }

    public Person deleteMinPriority() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }

        Person temp = arr[0];
        // System.arraycopy(arr, 1, arr, 0, --size); // Effektivare pga behöver ej
        // sortera om listan

        arr[0] = arr[size - 1];
        arr[size - 1] = null;
        size--;

        Quicksort.quickSort(arr, 0, size - 1);
        // Arrays.sort(arr, 0, size, Comparator.comparingInt(p -> p.prio));

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

        Quicksort.quickSort(arr, 0, size - 1);
        // Arrays.sort(arr, 0, size, Comparator.comparingInt(p -> p.prio));
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

class Quicksort {
    public static void quickSort(Person[] arr, int low, int high) {
        if (low < high) {
            int partitionIndex = partition(arr, low, high);

            quickSort(arr, low, partitionIndex - 1);
            quickSort(arr, partitionIndex + 1, high);
        }
    }

    private static int partition(Person[] arr, int low, int high) {
        int pivot = arr[high].getPriority();
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j].getPriority() <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, high);

        return i + 1;
    }

    private static void swap(Person[] arr, int i, int j) {
        Person temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
