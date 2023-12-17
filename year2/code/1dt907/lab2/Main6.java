import algorithms.sort.Shellsort;

import java.util.Random;
import java.util.Arrays;

public class Main6 {
    public static void main(String[] args) {
        Random rnd = new Random();
        int[] arr;

        for (int i = 1; i <= 10; i++) {
            arr = new int[100_000 * i];
            for (int j = 0; j < arr.length; j++) {
                arr[j] = rnd.nextInt();
            }
            System.out.println("Testing for array size of " + arr.length);
            test(arr);
        }
    }

    private static void test(int[] arr) {
        Timer sw = new Timer();

        int[] arr1 = Arrays.copyOf(arr, arr.length);
        int[] arr2 = Arrays.copyOf(arr, arr.length);
        int[] arr3 = Arrays.copyOf(arr, arr.length);

        String seq1 = "hibbard";
        String seq2 = "sedgewick";
        String seq3 = "knuth";

        sw.start();
        Shellsort.shellsort(arr1, seq1);
        sw.stop();
        System.out.println("ShellSort w seq: " + seq1 + ", time: " + sw.chooseTimePrefix(sw.getTimeInNanoSeconds()));

        sw.reset();

        sw.start();
        Shellsort.shellsort(arr2, seq2);
        sw.stop();
        System.out.println("ShellSort w seq: " + seq2 + ", time: " + sw.chooseTimePrefix(sw.getTimeInNanoSeconds()));

        sw.reset();

        sw.start();
        Shellsort.shellsort(arr3, seq3);
        sw.stop();
        System.out.println("ShellSort w seq: " + seq3 + ", time: " + sw.chooseTimePrefix(sw.getTimeInNanoSeconds()));

        System.out.println();
    }
}
