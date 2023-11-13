import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import algorithms.BruteForce3Sum;
import algorithms.TwoPointer3Sum;

// * Problem 7
public class Main3Sum {
    private static int MIN_SIZE = 1_000;
    private static int MAX_SIZE = 10_000;
    private static int SIZE_STEP = 1_000;
    private static int RND_SIZE = 100_000;

    private static List<Double> BFTimes = new ArrayList<>();
    private static List<Double> TPTimes = new ArrayList<>();

    private static List<List<Integer>> result;

    public static void main(String[] args) {
        TitlePrint.printTask("Problem 7");

        Random random = new Random();
        Timer sw = new Timer();

        for (int size = MIN_SIZE; size <= MAX_SIZE; size += SIZE_STEP) {
            int[] nums = new int[size];
            for (int i = 0; i < size; i++) {
                nums[i] = random.nextInt(2 * RND_SIZE + 1) - RND_SIZE;
            }

            System.out.println("# of Objects: " + size);

            sw.start();
            result = BruteForce3Sum.threeSum(nums);
            sw.stop();

            printResult("Bruteforce", sw.getTimeInNanoSeconds(), result, sw);

            clear(sw, result);

            sw.start();
            result = TwoPointer3Sum.threeSum(nums);
            sw.stop();

            printResult("Two-Pointer", sw.getTimeInNanoSeconds(), result, sw);

            clear(sw, result);

            System.out.println("");
        }

        WriteJSON.writeJSON(BFTimes, "Bruteforce");
        WriteJSON.writeJSON(TPTimes, "Two-Pointer");
    }

    /**
     * Prints the result of the algorithm execution.
     *
     * @param algorithm   the name of the algorithm used
     * @param elapsedTime the execution time in milliseconds(can be adjusted)
     * @param result      the list of triplets found
     */
    private static void printResult(String algorithm, double elapsedTime, List<List<Integer>> result, Timer sw) {
        System.out.println(algorithm + ":");
        System.out.println("Execution time: " + sw.chooseTimePrefix(elapsedTime));
        System.out.println("Number of triplets found: " + result.size() + "\n");

        if (algorithm == "Bruteforce") {
            BFTimes.add(elapsedTime);
        } else {
            TPTimes.add(elapsedTime);
        }
    }

    /**
     * Clears the given timer and result list.
     *
     * @param sw     the timer is reset
     * @param result the list is cleared
     */
    private static void clear(Timer sw, List<List<Integer>> result) {
        sw.reset();
        result.clear();
    }
}
