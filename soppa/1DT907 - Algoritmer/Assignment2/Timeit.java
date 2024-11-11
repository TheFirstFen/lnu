package Assignment2;

public class Timeit {
    public static Double timeCode(Runnable code, Integer amount, Boolean printResult) {
        Long start = System.nanoTime();

        for (Integer i = 0; i < amount; i++) {
            code.run();
        }

        Long end = System.nanoTime();

        Long time = end - start;
        double seconds = (double) time / 1_000_000.0;


        if (printResult) {
            System.out.println(seconds + " Milliseconds");
        }

        return seconds;
    }
}


