import algorithms.Percolation;

public class Main8 {
    public static void main(String[] args) {
        TitlePrint.printTask("Problem 8");

        int n = Integer.parseInt(args[0]);
        int exp = Integer.parseInt(args[1]);

        double[] thresholds = new double[exp];

        for (int i = 0; i < exp; i++) {
            Percolation percolation = new Percolation(n);

            while (!percolation.percolates()) {
                int row = uniform(n);
                int col = uniform(n);

                if (!percolation.isOpen(row, col)) {
                    percolation.open(row, col);
                }
            }

            thresholds[i] = (double) percolation.openSites / (n * n);
            System.out.println("Run(" + (i + 1) + ") Percolation threshold for " + n + " objects: " + (i + 1) + ": "
                    + thresholds[i]);
        }

        double mean = mean(thresholds);
        double stddev = std(thresholds);

        System.out.println("Mean percolation threshold: " + mean);
        System.out.println("Standard deviation: " + stddev);
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
