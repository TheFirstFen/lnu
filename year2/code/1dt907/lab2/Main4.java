import algorithms.sort.*;

import java.util.Arrays;
import java.util.Random;

public class Main4 {
    public static void main(String[] args) {
        Random rnd = new Random();
        int[] arr = new int[1_000];

        for (int j = 5; j <= 100; j += 5) {

            for (int i = 0; i < arr.length; i++)
                arr[i] = rnd.nextInt();

            for (int i = 0; i < 1; i++)
                System.out.println(test(arr, j) + " for recursion depth: " + j);
        }
    }

    private static String test(int[] arr, int depth) {
        Timer sw = new Timer();

        Quicksort.quickSort(arr, depth);

        int[] arrI = Arrays.copyOf(arr, arr.length);
        int[] arrH = Arrays.copyOf(arr, arr.length);

        double timeI, timeH;

        sw.start();
        Insertionsort.insertionsort(arrI, 0, arrI.length - 1);
        sw.stop();
        timeI = sw.getTimeInNanoSeconds();

        sw.reset();

        sw.start();
        Heapsort.heapsort(arrH);
        sw.stop();
        timeH = sw.getTimeInNanoSeconds();

        if (timeH <= timeI) {
            return "Heapsort is the most efficient algoritm with time: " + sw.chooseTimePrefix(timeH) + " and";
        } else {
            return "Insertionsort is the most efficient algorithm with time: " + sw.chooseTimePrefix(timeI) + " and";
        }
    }
}
