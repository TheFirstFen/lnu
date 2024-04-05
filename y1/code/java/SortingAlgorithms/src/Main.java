import java.lang.Math; // Importing the math library

public class Main {
    public static void main(String[] args) {
        double[] bubbleSort = new double[100_000]; // Creating four arrays to store data points in
        double[] insertionSort = new double[100_000];
        double[] mergeSort = new double[1_000_000];
        double[] quickSort = new double[1_000_000];

        for (int i = 0; i < 100_000; i++) // These four for loops fill all the arrays with random data points
            bubbleSort[i] = Math.random();

        for (int i = 0; i < 100_000; i++)
            insertionSort[i] = Math.random();

        for (int i = 0; i < 1_000_000; i++)
            mergeSort[i] = Math.random();

        for (int i = 0; i < 1_000_000; i++)
            quickSort[i] = Math.random();

        Timer sw = new Timer(); // Generates a stopwatch

        // Creates time variables one for each type of sorting algorithm
        double bubbleTime, insertionTime, mergeTime, quickTime;

        sw.start(); // Starts the stopwatch
        Bubblesort.bubbleSort(bubbleSort); // Calls the class.function
        sw.stop(); // Stops the stopwatch
        bubbleTime = sw.getTimeInNanoSeconds(); // Gets the elapsed time in the milliseconds unit
        sw.reset(); // Resets the stopwatch
        System.out.println("Bubble sort Done!");

        sw.start();
        Insertionsort.insertionSort(insertionSort);
        sw.stop();
        insertionTime = sw.getTimeInNanoSeconds();
        sw.reset();
        System.out.println("Insertion sort Done!");

        sw.start();
        Mergesort.mergeSort(mergeSort);
        sw.stop();
        mergeTime = sw.getTimeInNanoSeconds(); // Gets the elapsed time in the microseconds unit
        sw.reset();
        System.out.println("Mergesort Done!");

        sw.start();
        Quicksort.quickSort(quickSort);
        sw.stop();
        quickTime = sw.getTimeInNanoSeconds();
        sw.reset();
        System.out.println("Quicksort Done!");

        // Prints the result times for each sorting algorithm
        System.out.println("Bubble sort: " + sw.chooseTimePrefix(bubbleTime));
        System.out.println("Insertion sort: " + sw.chooseTimePrefix(insertionTime));
        System.out.println("Mergesort: " + sw.chooseTimePrefix(mergeTime));
        System.out.println("Quicksort: " + sw.chooseTimePrefix(quickTime));
    }
}
