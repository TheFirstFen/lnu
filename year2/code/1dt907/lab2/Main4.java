import algorithms.sort.*;
import java.util.Random;

public class Main4 {
    static int SIZE = 5_000_000;
    static int RND_SIZE = 1_000;
    static double[] TIME_I, TIME_H;
    static int ALGORITHM = 0; // * 0 - HeapSort, 1 - InsertionSort

    public static void main(String[] args) {
        Random rnd = new Random();
        int[] arr = new int[SIZE];
        for (int exp = 0; exp < 1; exp++) {
            TIME_I = new double[21];
            TIME_H = new double[21];
            for (int i = 0; i < arr.length; i++)
                arr[i] = rnd.nextInt(RND_SIZE);
            for (int maxDepth = 5; maxDepth <= 100; maxDepth += 5) {
                Quicksort.quickSort(arr, maxDepth, ALGORITHM, TIME_I, TIME_H);
                String out = getTime(arr, maxDepth / 5);
                System.out.println(out + ", recursion depth: " + maxDepth + " | sorted: " + isSorted(arr));
            }

            // System.out.println("Recommended Quicksort depth for Insersort: " +
            // minTime(TIME_I));
            // System.out.println("Recommended Quicksort depth for Heapsort: " +
            // minTime(TIME_H));

            for (int i = 1; i < TIME_H.length; i++) {
                // System.out.println("Depth: " + (i * 5) + " | Insertionsort: " +
                // sw.chooseTimePrefix(TIME_I[i]) + " | Heapsort: " +
                // sw.chooseTimePrefix(TIME_H[i]));
            }
        }

        if (isSorted(arr)) {
            System.out.println("Sorted!");
        } else {
            System.out.println("Not sorted!");
        }
    }

    private static String getTime(int[] arr, int exp) {
        Timer sw = new Timer();

        if (TIME_H[exp] <= TIME_I[exp]) {
            return "Heapsort most efficient: " + sw.chooseTimePrefix(TIME_H[exp]);
        } else {
            return "Insertionsort most efficient: " + sw.chooseTimePrefix(TIME_I[exp]);
        }
    }

    private static String minTime(double[] arr) {
        double min = arr[1];
        int minIdx = 0;

        for (int i = 2; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
                minIdx = i;
            }
        }

        return Integer.toString(minIdx * 5);
    }

    private static boolean isSorted(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                return false;
            }
        }
        return true;
    }
}