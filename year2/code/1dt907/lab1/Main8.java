import java.util.ArrayList;
import java.util.List;

import algorithms.Percolation;

public class Main8 {
    public static void main(String[] args) {
        Timer runTime = new Timer();
        runTime.start();

        TitlePrint.printTask("Problem 8");

        if (args.length != 2) {
            System.out.println("Usage: java Main8 <# objects> <experiments>");
            System.exit(1);
        }

        int n = Integer.parseInt(args[0]);
        int exp = Integer.parseInt(args[1]);

        Timer sw = new Timer();

        double[] thresholds = new double[exp];
        List<Double> time = new ArrayList<>();

        runPercolation(exp, n, sw, thresholds, time);

        WriteJSON.writeJSON(time, "Percolation");

        runTime.stop();

        TitlePrint.printTask(runTime.chooseTimePrefix(runTime.getTimeInNanoSeconds()));
    }

    private static void runPercolation(int exp, int n, Timer sw, double[] thresholds, List<Double> time) {
        for (int i = 0; i < exp; i++) {
            Percolation percolation = new Percolation(n);

            sw.start();

            while (!percolation.percolates()) {
                int row = uniform(n);
                int col = uniform(n);

                if (!percolation.isOpen(row, col)) {
                    percolation.open(row, col);
                }
            }

            sw.stop();

            thresholds[i] = (double) percolation.openSites / (n * n);
            System.out.println("Run(" + (i + 1) + "): Percolation threshold for " + n + " objects: "
                    + thresholds[i] + ". Took " + sw.chooseTimePrefix(sw.getTimeInNanoSeconds()));

            time.add(sw.getTimeInNanoSeconds());

            sw.reset();
        }

        double meanTime = mean(convertArrayListToArray(time));
        double mean = mean(thresholds);
        double std = std(thresholds);

        System.out.println("\nMean time taken: " + sw.chooseTimePrefix(meanTime));
        System.out.println("Mean percolation threshold: " + mean);
        System.out.println("Standard deviation: " + std);
    }

    private static double[] convertArrayListToArray(List<Double> time) {
        int size = time.size();
        double[] data = new double[size];

        for (int i = 0; i < size; i++) {
            data[i] = time.get(i);
        }

        return data;
    }

    private static double mean(double[] data) {
        double sum = 0;

        for (double value : data) {
            sum += value;
        }

        return sum / data.length;
    }

    private static double std(double[] data) {
        double mean = mean(data);
        double sum = 0;

        for (double value : data) {
            sum += Math.pow(value - mean, 2);
        }

        return Math.sqrt(sum / (data.length - 1));
    }

    private static int uniform(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("Must be >=0");
        }

        return (int) (Math.random() * n) + 1;
    }
}
