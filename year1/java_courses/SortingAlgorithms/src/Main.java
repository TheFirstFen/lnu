import java.lang.Math;                              // Importing the math library
import java.util.concurrent.TimeUnit;               // Importing the timeunit library
import org.apache.commons.lang3.time.StopWatch;     // Importing the stopwatch library

public class Main {
    public static void main(String[] args) {
        double[] bubbleSort = new double[100000];   // Creating four arrays to store data points in
        double[] insertionSort = new double[100000];
        double[] mergeSort = new double[100000];
        double[] quickSort = new double[100000];

        for (int i = 0; i < 100000; i++)            // These four for loops fill all the arrays with random data points
            bubbleSort[i] = Math.random();

        for (int i = 0; i < 100000; i++)
            insertionSort[i] = Math.random();

        for (int i = 0; i < 100000; i++)
            mergeSort[i] = Math.random();

        for (int i = 0; i < 100000; i++)
            quickSort[i] = Math.random();

        StopWatch stopWatch = new StopWatch();      // Generates a stopwatch

        // Creates time variables one for each type of sorting algorithm
        double bubbleTime, insertionTime, mergeTime, quickTime;

        stopWatch.start();                          // Starts the stopwatch
        Bubblesort.bubbleSort(bubbleSort);          // Calls the class.function
        stopWatch.stop();                           // Stops the stopwatch
        bubbleTime = stopWatch.getTime(TimeUnit.MILLISECONDS);  // Gets the elapsed time in the milliseconds unit
        stopWatch.reset();                          // Resets the stopwatch
        System.out.println("Bubble sort Done!");

        stopWatch.start();
        Insertionsort.insertionSort(insertionSort);
        stopWatch.stop();
        insertionTime = stopWatch.getTime(TimeUnit.MILLISECONDS);
        stopWatch.reset();
        System.out.println("Insertion sort Done!");

        stopWatch.start();
        Mergesort.mergeSort(mergeSort);
        stopWatch.stop();
        mergeTime = stopWatch.getTime(TimeUnit.MICROSECONDS);   // Gets the elapsed time in the microseconds unit
        stopWatch.reset();
        System.out.println("Mergesort Done!");

        stopWatch.start();
        Quicksort.quickSort(quickSort);
        stopWatch.stop();
        quickTime = stopWatch.getTime(TimeUnit.MICROSECONDS);
        stopWatch.reset();
        System.out.println("Quicksort Done!");

        // Prints the result times for each sorting algorithm
        System.out.println("Bubble sort: " + bubbleTime + " milliseconds");
        System.out.println("Insertion sort: " + insertionTime + " milliseconds");
        System.out.println("Mergesort: " + mergeTime + " microseconds");
        System.out.println("Quicksort: " + quickTime + " microseconds");
    }
}
