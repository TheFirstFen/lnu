import algorithms.sort.*;
import java.util.Random;

public class Main4 {
    static int SIZE = 5_000_000;
    static int RND_SIZE = 1_000;
    static int INCREMENTS = 5; // * Adjust if other tests needed
    static double[] TIME_I, TIME_H;
    static int ALGORITHM = 0; // * 0 - HeapSort, 1 - InsertionSort

    public static void main(String[] args) {
        Timer sw = new Timer();
        Random rnd = new Random();
        int[] arr = new int[SIZE];
        for (int exp = 0; exp < 1; exp++) {
            TIME_I = new double[21];
            TIME_H = new double[21];

            for (int i = 0; i < arr.length; i++)
                arr[i] = rnd.nextInt(RND_SIZE);

            // Heapsort after quicksort
            for (int maxDepth = INCREMENTS; maxDepth <= INCREMENTS * 20; maxDepth += INCREMENTS) {
                sw.start();
                Quicksort.quickSort(arr.clone(), maxDepth, ALGORITHM);
                sw.stop();
                TIME_H[maxDepth / INCREMENTS] = sw.getTimeInNanoSeconds();
                sw.reset();
            }

            // Insertsort after quicksort
            ALGORITHM = 1;
            for (int maxDepth = INCREMENTS; maxDepth <= INCREMENTS * 20; maxDepth += INCREMENTS) {
                sw.start();
                Quicksort.quickSort(arr.clone(), maxDepth, ALGORITHM);
                sw.stop();
                TIME_I[maxDepth / INCREMENTS] = sw.getTimeInNanoSeconds();
                sw.reset();
            }

            for (int i = 1; i < TIME_H.length; i++) {
                // System.out.println("Depth: " + (i * 5) + " | Insertionsort: " +
                // sw.chooseTimePrefix(TIME_I[i]) + " | Heapsort: " +
                // sw.chooseTimePrefix(TIME_H[i]));

                String out = getTimeForEachDepth(arr, i);
                System.out.println(out + ", recursion depth: " + (i * INCREMENTS));
            }

            System.out.println("Recommended Quicksort depth for Insersort: " + recomendedDepth(TIME_I));
            System.out.println("Recommended Quicksort depth for Heapsort: " + recomendedDepth(TIME_H));
        }
    }

    private static String getTimeForEachDepth(int[] arr, int exp) {
        Timer sw = new Timer();

        if (TIME_H[exp] <= TIME_I[exp]) {
            return "Heapsort most efficient: " + sw.chooseTimePrefix(TIME_H[exp]);
        } else {
            return "Insertionsort most efficient: " + sw.chooseTimePrefix(TIME_I[exp]);
        }
    }

    private static String recomendedDepth(double[] arr) {
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
}