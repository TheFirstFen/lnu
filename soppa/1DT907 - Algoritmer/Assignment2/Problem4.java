package Assignment2;

import java.util.ArrayList;
import java.util.Random;
import java.util.List;


public class Problem4 {

    public static void main(String[] args) {
        int amount = 100000;
        List<Double> insertResults = new ArrayList<>();
        List<Double> heapResults = new ArrayList<>();
        for (int depth = 10; depth <= 50; depth = depth + 5) {
            int n = 0;
            int[] myarray = new int[amount];
            Random random = new Random();
            while (n < amount) {
                myarray[n] = random.nextInt(amount);
                n ++;
            }
            
    
            QuickSort quickSort = new QuickSort(depth, "insert");
            Runnable code = () -> quickSort.sort(myarray);
            Double time = Timeit.timeCode(code, 1, false);
            insertResults.add(time);
            System.out.println("Time to sort 100000 random values using insertSort after a maximum of " + depth + " recursions of quicksort");
            System.out.println(time);
        }
        System.out.println("------------------------------");
        for (int depth = 10; depth <= 50; depth = depth + 5) {
            int n = 0;
            int[] myarray = new int[amount];
            Random random = new Random();
            while (n < amount) {
                myarray[n] = random.nextInt(amount);
                n ++;
            }
            
            
            QuickSort quickSort = new QuickSort(depth, "heap");
            Runnable code = () -> quickSort.sort(myarray);
            Double time = Timeit.timeCode(code, 1, false);
            heapResults.add(time);
            System.out.println("Time to sort 100000 random values using heapsort after " + depth + " recursions of quicksort");
            System.out.println(time);
        }

        System.out.println("---------------------------");
        int temp = 0;
        String quickest;
        for (int depth = 10; depth <= 50; depth = depth + 5) {
            if (insertResults.get(temp) < heapResults.get(temp)) {
                quickest = "insertSort";
            } else {
                quickest = "heapSort";
            }
            System.out.println("For the depth " + depth + " "  + quickest + " is faster");
            temp ++;
        }
    }
    
}
