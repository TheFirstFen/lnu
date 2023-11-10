import java.util.Random;
import java.util.List;
import java.util.ArrayList;

import algorithms.UnionFind;
import algorithms.WQUnionFind;
import algorithms.PCWQUnionFind;
import algorithms.QUnionFind;

// * Problem 4
public class MainUF {
    protected static int unionTestSize = 10_000;
    protected static int listSize = 100_000;

    public static void main(String[] args) {
        Random rnd = new Random();
        Timer sw = new Timer();

        TitlePrint.printTask("Problem 4");

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

            for (int j = 0; j < 10; j++) {
                if (unionTestSize * (j + 1) > listSize * (i + 1))
                    break;
                UnionFind quickFind = new UnionFind(listSize * (i + 1));
                QUnionFind quickUnion = new QUnionFind(listSize * (i + 1));
                WQUnionFind weightedQuickUnion = new WQUnionFind(listSize * (i + 1));
                PCWQUnionFind pathCompressionWeightedQuickUnion = new PCWQUnionFind(listSize * (i + 1));

                System.out.println("\nList size: " + listSize * (i + 1) + ", Unions: " + unionTestSize * (j + 1));
                sw.start();
                quickFindTest(quickFind, unionTestSize * (j + 1), rnd);
                sw.stop();
                tempUF.add(sw.getTimeInMilliSeconds());
                System.out.println("Run (" + (j + 1) + "): Elapsed time (UF): " + sw.getTimeInMilliSeconds() + " ms");

                sw.reset();

                sw.start();
                quickUnionTest(quickUnion, unionTestSize * (j + 1), rnd);
                sw.stop();
                tempQUF.add(sw.getTimeInMilliSeconds());
                System.out.println("Run (" + (j + 1) + "): Elapsed time (QUF): " + sw.getTimeInMilliSeconds() + " ms");

                sw.reset();

                sw.start();
                weightedQuickUnionTest(weightedQuickUnion, unionTestSize * (j + 1), rnd);
                sw.stop();
                tempWQUF.add(sw.getTimeInMilliSeconds());
                System.out.println("Run (" + (j + 1) + "): Elapsed time (WQUF): " + sw.getTimeInMilliSeconds() + " ms");

                sw.reset();

                sw.start();
                pathCompressionWeightedQuickUnionTest(pathCompressionWeightedQuickUnion, unionTestSize * (j + 1), rnd);
                sw.stop();
                tempPCWQUF.add(sw.getTimeInMilliSeconds());
                System.out
                        .println("Run (" + (j + 1) + "): Elapsed time (PCWQUF): " + sw.getTimeInMilliSeconds() + " ms");
            }

            uf.add(tempUF);
            quf.add(tempQUF);
            wquf.add(tempWQUF);
            pcwquf.add(tempPCWQUF);
        }

        // System.out.println(uf.toString()); // Used for collecting datapoints
        // System.out.println(quf.toString()); // Used for collecting datapoints
        // System.out.println(wquf.toString()); // Used for collecting datapoints
        // System.out.println(pcwquf.toString()); // Used for collecting datapoints
    }

    private static void quickFindTest(UnionFind quickFind, int size, Random rnd) {
        for (int i = 0; i < size; i++) {
            int a = rnd.nextInt(listSize);
            int b = rnd.nextInt(listSize);
            if (!quickFind.connected(a, b))
                quickFind.union(a, b);
        }
    }

    private static void quickUnionTest(QUnionFind quickUnion, int size, Random rnd) {
        for (int i = 0; i < size; i++) {
            int a = rnd.nextInt(listSize);
            int b = rnd.nextInt(listSize);
            if (!quickUnion.connected(a, b))
                quickUnion.union(a, b);
        }
    }

    private static void weightedQuickUnionTest(WQUnionFind weightedQuickUnion, int size, Random rnd) {
        for (int i = 0; i < size; i++) {
            int a = rnd.nextInt(listSize);
            int b = rnd.nextInt(listSize);
            if (!weightedQuickUnion.connected(a, b))
                weightedQuickUnion.union(a, b);
        }
    }

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