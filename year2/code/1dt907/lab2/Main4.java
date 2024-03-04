import algorithms.sort.*;
import java.util.Random;

public class Main4 {
    static int SIZE = 500_000;
    static int RND_SIZE = 1_000;
    static double[] timeI, timeH;

    public static void main(String[] args) {
        Timer sw = new Timer();
        Random rnd = new Random();
        int[] arr = new int[SIZE];
        for (int exp = 0; exp < 1; exp++) {
            timeI = new double[21];
            timeH = new double[21];
            for (int i = 0; i < arr.length; i++)
                arr[i] = rnd.nextInt(RND_SIZE);
            for (int maxDepth = 5; maxDepth <= 100; maxDepth += 5) {
                Quicksort.quickSort(arr, maxDepth, timeI, timeH);
                String out = getTime(arr, maxDepth / 5);
                System.out.println(out + ", recursion depth: " + maxDepth);
            }

            System.out.println("Recommended Quicksort depth for Insersort: " + minTime(timeI));
            System.out.println("Recommended Quicksort depth for Heapsort: " + minTime(timeH));

            for (int i = 1; i < timeH.length; i++) {
                System.out.println("Depth: " + (i * 5) + " | Insertionsort: " + sw.chooseTimePrefix(timeI[i])
                        + " | Heapsort: " + sw.chooseTimePrefix(timeH[i]));
            }
        }
    }

    private static String getTime(int[] arr, int exp) {
        Timer sw = new Timer();

        if (timeH[exp] <= timeI[exp]) {
            return "Heapsort most efficient: " + sw.chooseTimePrefix(timeH[exp]);
        } else {
            return "Insertionsort most efficient: " + sw.chooseTimePrefix(timeI[exp]);
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