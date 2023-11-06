import java.util.Random;
import java.util.List;
import java.util.ArrayList;

import algorithms.QUnionFind;
import algorithms.WQUnionFind;

// * Problem 4
public class MainUF {
    protected static int unionTestSize = 1_000_0;
    protected static int listSize = 1_000_00;

    public static void main(String[] args) {
        Random rnd = new Random();
        Timer sw = new Timer();

        TitlePrint.printTask("Problem 4");

        List<List<Double>> quf = new ArrayList<>();
        List<List<Double>> wquf = new ArrayList<>();

        for (int i = 0; i < 10; i++) {
            List<Double> tempQUF = new ArrayList<>();
            List<Double> tempWQUF = new ArrayList<>();

            System.out.println("\nList size: " + listSize * (i + 1));

            for (int j = 0; j < 10; j++) {
                QUnionFind quickFind = new QUnionFind(listSize * (i + 1));
                WQUnionFind weightedQuickFind = new WQUnionFind(listSize * (i + 1));

                System.out.println("\nList size: " + listSize * (i + 1) + ", Unions: " + unionTestSize * (j + 1));
                sw.start();
                quickFindTest(quickFind, unionTestSize * (j + 1), rnd);
                sw.stop();
                tempQUF.add(sw.getTimeInMilliSeconds());
                System.out.println("Run (" + (j + 1) + "): Elapsed time (QUF): " + sw.getTimeInSeconds() + " s");

                sw.reset();

                sw.start();
                weightedQuickFindTest(weightedQuickFind, unionTestSize * (j + 1), rnd);
                sw.stop();
                tempWQUF.add(sw.getTimeInMilliSeconds());
                System.out.println("Run (" + (j + 1) + "): Elapsed time (WQUF): " + sw.getTimeInMilliSeconds() + " ms");
            }

            quf.add(tempQUF);
            wquf.add(tempWQUF);
        }

        System.out.println(quf.toString());
        System.out.println(wquf.toString());
    }

    private static void quickFindTest(QUnionFind quickFind, int size, Random rnd) {
        for (int i = 0; i < size; i++) {
            int a = rnd.nextInt(listSize);
            int b = rnd.nextInt(listSize);
            if (!quickFind.connected(a, b))
                quickFind.union(a, b);
        }
    }

    private static void weightedQuickFindTest(WQUnionFind weightedQuickFind, int size, Random rnd) {
        for (int i = 0; i < size; i++) {
            int a = rnd.nextInt(listSize);
            int b = rnd.nextInt(listSize);
            if (!weightedQuickFind.connected(a, b))
                weightedQuickFind.union(a, b);
        }
    }
}