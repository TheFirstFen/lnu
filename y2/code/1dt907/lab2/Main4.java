import algorithms.sort.*;
import java.util.Random;

public class Main4 {
    static final int SIZE = 100_000;
    static final int RND_SIZE = SIZE / 50;
    static final int INCREMENTS = 5; // * Adjust if other tests needed
    static final int EXPERIMENTS = 100;
    static int heapsortPerExp;
    static int insertsortPerExp;
    static int heapsort;
    static int insertsort;
    static double[] TIME_I, TIME_H;
    static boolean ALGORITHM = false; // * false - HeapSort, true - InsertionSort
    static String Winner;

    public static void main(String[] args) {
        Timer sw = new Timer();
        Random rnd = new Random();
        int[] arr = new int[SIZE];
        for (int exp = 0; exp < EXPERIMENTS; exp++) {
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
            ALGORITHM = true;
            for (int maxDepth = INCREMENTS; maxDepth <= INCREMENTS * 20; maxDepth += INCREMENTS) {
                sw.start();
                Quicksort.quickSort(arr.clone(), maxDepth, ALGORITHM);
                sw.stop();
                TIME_I[maxDepth / INCREMENTS] = sw.getTimeInNanoSeconds();
                sw.reset();
            }

            // * Deprecated code
            // for (int i = 1; i < TIME_H.length; i++) {
            // fullInfoPrint(i, sw);
            // bestPerDepth(arr, i, sw);
            // }

            System.out.println("Recommended Quicksort depth for Insersort: " + recomendedDepth(TIME_I));
            System.out.println("Recommended Quicksort depth for Heapsort: " + recomendedDepth(TIME_H) + "\n");

            if (insertsortPerExp > heapsortPerExp) {
                insertsort++;
                Winner = "Insertionsort";
            } else {
                heapsort++;
                Winner = "Heapsort";
            }

            // System.out.println("\nThe more efficient algorithm throughout: " + Winner);
        }

        System.out.println("Heapsort won: " + heapsort + " experiments");
        System.out.println("Insertionsort won: " + insertsort + " experiments");
    }

    private static String getTimeForEachDepth(int[] arr, int exp, Timer sw) {
        if (TIME_H[exp] <= TIME_I[exp]) {
            heapsortPerExp++;
            return "Heapsort most efficient: " + sw.chooseTimePrefix(TIME_H[exp]);
        } else {
            insertsortPerExp++;
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

        return Integer.toString(minIdx * INCREMENTS);
    }

    // * Unused
    private static void fullInfoPrint(int i, Timer sw) { // * Deprecated code
        System.out.println(
                "Depth: " + (i * INCREMENTS) + " | Insertionsort: " + sw.chooseTimePrefix(TIME_I[i]) + " | Heapsort: "
                        + sw.chooseTimePrefix(TIME_H[i]) + "\n");
    }

    // * Unused
    private static void bestPerDepth(int[] arr, int i, Timer sw) { // * Deprecated code
        String out = getTimeForEachDepth(arr, i, sw);
        System.out.println(out + ", recursion depth: " + (i * INCREMENTS));
        System.out.println("-------------");

    }
}