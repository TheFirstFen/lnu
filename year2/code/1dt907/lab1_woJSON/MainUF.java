import java.util.Random;
import java.util.List;
import java.util.ArrayList;

import algorithms.UnionFind;
import algorithms.WQUnionFind;
import algorithms.PCWQUnionFind;
import algorithms.QUnionFind;

// * Problem 4
public class MainUF {
    private static int unionTestSize = 10_000;
    private static int listSize = 100_000;

    public static void main(String[] args) {
        Timer runTime = new Timer();
        runTime.start();

        TitlePrint.printTask("Problem 4");

        Random rnd = new Random();
        Timer sw = new Timer();

        List<List<Double>> uf = new ArrayList<>();
        List<List<Double>> quf = new ArrayList<>();
        List<List<Double>> wquf = new ArrayList<>();
        List<List<Double>> pcwquf = new ArrayList<>();

        for (int i = 0; i < 10; i++) {
            List<Double> tempUF = new ArrayList<>();
            List<Double> tempQUF = new ArrayList<>();
            List<Double> tempWQUF = new ArrayList<>();
            List<Double> tempPCWQUF = new ArrayList<>();

            System.out.println("\nList size: " + listSize * (i + 1));

            for (int j = 0; j < 9; j++) {
                if (unionTestSize * (j + 1) > listSize * (i + 1))
                    break;
                UnionFind quickFind = new UnionFind(listSize * (i + 1));
                QUnionFind quickUnion = new QUnionFind(listSize * (i + 1));
                WQUnionFind weightedQuickUnion = new WQUnionFind(listSize * (i + 1));
                PCWQUnionFind pathCompressionWeightedQuickUnion = new PCWQUnionFind(listSize * (i + 1));

                System.out.println("\nList size: " + listSize * (i + 1) + ", Unions: " + unionTestSize * (j + 1));

                runUF(sw, quickFind, j, rnd, tempUF);

                runQUF(sw, quickUnion, j, rnd, tempQUF);

                runWQUF(sw, weightedQuickUnion, j, rnd, tempWQUF);

                runPCWQUF(sw, pathCompressionWeightedQuickUnion, j, rnd, tempPCWQUF);
            }

            uf.add(tempUF);
            quf.add(tempQUF);
            wquf.add(tempWQUF);
            pcwquf.add(tempPCWQUF);
        }

        runTime.stop();

        TitlePrint.printTask("Runtime: " + runTime.chooseTimePrefix(runTime.getTimeInNanoSeconds()));
    }

    private static void runUF(Timer sw, UnionFind uf, int j, Random rnd, List<Double> time) {
        sw.start();
        quickFindTest(uf, unionTestSize * (j + 1), rnd);
        sw.stop();
        time.add(sw.getTimeInNanoSeconds());
        System.out.println(
                "Run (" + (j + 1) + "): Elapsed time (UF): " + sw.chooseTimePrefix(sw.getTimeInNanoSeconds()));

        sw.reset();
    }

    private static void runQUF(Timer sw, QUnionFind quf, int j, Random rnd, List<Double> time) {
        sw.start();
        quickUnionTest(quf, unionTestSize * (j + 1), rnd);
        sw.stop();
        time.add(sw.getTimeInNanoSeconds());
        System.out.println(
                "Run (" + (j + 1) + "): Elapsed time (QUF): " + sw.chooseTimePrefix(sw.getTimeInNanoSeconds()));

        sw.reset();
    }

    private static void runWQUF(Timer sw, WQUnionFind wquf, int j, Random rnd, List<Double> time) {
        sw.start();
        weightedQuickUnionTest(wquf, unionTestSize * (j + 1), rnd);
        sw.stop();
        time.add(sw.getTimeInNanoSeconds());
        System.out.println("Run (" + (j + 1) + "): Elapsed time (WQUF): "
                + sw.chooseTimePrefix(sw.getTimeInNanoSeconds()));

        sw.reset();
    }

    private static void runPCWQUF(Timer sw, PCWQUnionFind pcwquf, int j, Random rnd, List<Double> time) {
        sw.start();
        pathCompressionWeightedQuickUnionTest(pcwquf, unionTestSize * (j + 1), rnd);
        sw.stop();
        time.add(sw.getTimeInNanoSeconds());
        System.out
                .println("Run (" + (j + 1) + "): Elapsed time (PCWQUF): "
                        + sw.chooseTimePrefix(sw.getTimeInNanoSeconds()));

        sw.reset();
    }

    /**
     * Performs a test using an object of the UnionFind class.
     *
     * @param quickFind The UnionFind object to be tested.
     * @param size      Amount of unions to be preformed.
     * @param rnd       The Random object used to generate random numbers.
     */
    private static void quickFindTest(UnionFind quickFind, int size, Random rnd) {
        for (int i = 0; i < size; i++) {
            int a = rnd.nextInt(listSize);
            int b = rnd.nextInt(listSize);
            if (!quickFind.connected(a, b))
                quickFind.union(a, b);
        }
    }

    /**
     * Performs a test using an object of the QUnionFind class.
     *
     * @param quickUnion The QUnionFind object to be tested.
     * @param size       Amount of unions to be preformed.
     * @param rnd        The Random object used to generate random numbers.
     */
    private static void quickUnionTest(QUnionFind quickUnion, int size, Random rnd) {
        for (int i = 0; i < size; i++) {
            int a = rnd.nextInt(listSize);
            int b = rnd.nextInt(listSize);
            if (!quickUnion.connected(a, b))
                quickUnion.union(a, b);
        }
    }

    /**
     * Performs a test using an object of the WQUnionFind class.
     *
     * @param weightedQuickUnion The WQUnionFind object to be tested.
     * @param size               Amount of unions to be preformed.
     * @param rnd                The Random object used to generate random numbers.
     */
    private static void weightedQuickUnionTest(WQUnionFind weightedQuickUnion, int size, Random rnd) {
        for (int i = 0; i < size; i++) {
            int a = rnd.nextInt(listSize);
            int b = rnd.nextInt(listSize);
            if (!weightedQuickUnion.connected(a, b))
                weightedQuickUnion.union(a, b);
        }
    }

    /**
     * Performs a test using an object of the PCWQUnionFind class.
     *
     * @param pathCompressionQuickUnion The PCWQUnionFind object to be tested.
     * @param size                      Amount of unions to be preformed.
     * @param rnd                       The Random object used to generate random
     *                                  numbers.
     */
    private static void pathCompressionWeightedQuickUnionTest(PCWQUnionFind pathCompressionQuickUnion, int size,
            Random rnd) {
        for (int i = 0; i < size; i++) {
            int a = rnd.nextInt(listSize);
            int b = rnd.nextInt(listSize);
            if (!pathCompressionQuickUnion.connected(a, b))
                pathCompressionQuickUnion.union(a, b);
        }
    }
}