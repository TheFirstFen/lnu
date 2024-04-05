import java.util.Random;

import algorithms.tree.*;

public class Main2 {
    static int TREE_SIZE = 10_000_000;
    static int TEST_SIZE = 1_000_000;
    static int SMALL_TEST = (int) Math.pow(2, 14) - 1;

    public static void main(String[] args) {
        BST bst = new BST();
        AVL avl = new AVL();
        Random rnd = new Random();
        Timer sw = new Timer();

        System.out.print("Generating realistic trees... ");
        for (int i = 0; i < TREE_SIZE; i++) {
            int temp = rnd.nextInt();

            bst.insert(temp);
            avl.insert(temp);
        }
        bst.insert(0);
        avl.insert(0);

        System.out.println(": Completed");

        System.out.println("BST height: " + bst.status());
        System.out.println("AVL height: " + avl.status());

        System.out.print("\nGenerating test values... ");
        int[] testVals = new int[TEST_SIZE];
        for (int i = 0; i < TEST_SIZE; i++) {
            testVals[i] = rnd.nextInt();
        }
        testVals[TEST_SIZE - 1] = 0;
        System.out.println(": Completed");

        System.out.println("\nStarting tests... ");
        System.out.println("General case:");
        test(bst, avl, sw, testVals);
        System.out.println("\n\nWorst case: ");
        worstCaseTest(sw, SMALL_TEST);
        System.out.println("\n\nBest case:");
        bestCaseTest(sw, SMALL_TEST);
        System.out.println("Tests : Completed");
    }

    private static void test(BST bst, AVL avl, Timer sw, int[] arr) {
        System.out.println("Time to insert, search & delete " + arr.length + " objects");

        double[] bstTimes = new double[3];
        double[] avlTimes = new double[3];

        sw.start();
        for (int i : arr) {
            bst.insert(i);
        }
        sw.stop();
        bstTimes[0] = sw.getTimeInNanoSeconds();

        sw.reset();

        sw.start();
        for (int i : arr) {
            bst.search(i);
        }
        sw.stop();
        bstTimes[1] = sw.getTimeInNanoSeconds();

        sw.reset();

        int bstStatus = bst.status();

        sw.start();
        for (int i : arr) {
            bst.delete(i);
        }
        sw.stop();
        bstTimes[2] = sw.getTimeInNanoSeconds();

        sw.reset();
        System.out.println("BST test: completed");

        sw.start();
        for (int i : arr) {
            avl.insert(i);
        }
        sw.stop();
        avlTimes[0] = sw.getTimeInNanoSeconds();

        sw.reset();

        sw.start();
        for (int i : arr) {
            avl.search(i);
        }
        sw.stop();
        avlTimes[1] = sw.getTimeInNanoSeconds();

        sw.reset();

        int avlStatus = avl.status();

        sw.start();
        for (int i : arr) {
            avl.delete(i);
        }
        sw.stop();
        avlTimes[2] = sw.getTimeInNanoSeconds();

        sw.reset();
        System.out.println("AVL test: completed\n");

        System.out.println("BST:");
        System.out.println(
                "insert: " + sw.chooseTimePrefix(bstTimes[0]) + "\nsearch: " + sw.chooseTimePrefix(bstTimes[1])
                        + "\ndelete: " + sw.chooseTimePrefix(bstTimes[2]) + "\nheight: " + bstStatus);

        System.out.println("\nAVL:");
        System.out.println(
                "insert: " + sw.chooseTimePrefix(avlTimes[0]) + "\nsearch: " + sw.chooseTimePrefix(avlTimes[1])
                        + "\ndelete: " + sw.chooseTimePrefix(avlTimes[2]) + "\nheight: " + avlStatus);

        System.out.println("\nDiff (AVL - BST):");
        System.out.println("insert: " + sw.chooseTimePrefix(avlTimes[0] - bstTimes[0]) + "\nsearch: "
                + sw.chooseTimePrefix(avlTimes[1] - bstTimes[1])
                + "\ndelete: " + sw.chooseTimePrefix(avlTimes[2] - bstTimes[2]) + "\nheight: "
                + (avlStatus - bstStatus));
    }

    private static void worstCaseTest(Timer sw, int testSize) {
        BST bst = new BST();
        AVL avl = new AVL();

        int[] arr = new int[testSize];

        for (int i = 0; i < testSize; i++) {
            arr[i] = i;
        }

        test(bst, avl, sw, arr);
    }

    private static void bestCaseTest(Timer sw, int testSize) {
        BST bst = new BST();
        AVL avl = new AVL();

        double[] bstTimes = new double[3];
        double[] avlTimes = new double[3];

        sw.reset();

        System.out.println("Time to insert, search & delete " + testSize + " objects");

        int[] arr = new int[testSize];
        for (int i = 0; i < testSize; i++)
            arr[i] = i;

        sw.start();
        bst = bst.generateBalancedTree(arr);
        sw.stop();
        bstTimes[0] = sw.getTimeInNanoSeconds();

        sw.reset();

        sw.start();
        for (int i : arr) {
            bst.search(i);
        }
        sw.stop();
        bstTimes[1] = sw.getTimeInNanoSeconds();

        sw.reset();

        int bstStatus = bst.status();

        sw.start();
        for (int i : arr) {
            bst.delete(i);
        }
        sw.stop();
        bstTimes[2] = sw.getTimeInNanoSeconds();

        sw.reset();
        System.out.println("BST test: completed");

        sw.start();
        avl = avl.generateBalancedTree(arr);
        sw.stop();
        avlTimes[0] = sw.getTimeInNanoSeconds();

        sw.reset();

        sw.start();
        for (int i : arr) {
            avl.search(i);
        }
        sw.stop();
        avlTimes[1] = sw.getTimeInNanoSeconds();

        sw.reset();

        int avlStatus = avl.status();

        sw.start();
        for (int i : arr) {
            avl.delete(i);
        }
        sw.stop();
        avlTimes[2] = sw.getTimeInNanoSeconds();

        sw.reset();
        System.out.println("AVL test: completed\n");

        System.out.println("BST:");
        System.out.println(
                "insert: " + sw.chooseTimePrefix(bstTimes[0]) + "\nsearch: " + sw.chooseTimePrefix(bstTimes[1])
                        + "\ndelete: " + sw.chooseTimePrefix(bstTimes[2]) + "\nheight: " + bstStatus);

        System.out.println("\nAVL:");
        System.out.println(
                "insert: " + sw.chooseTimePrefix(avlTimes[0]) + "\nsearch: " + sw.chooseTimePrefix(avlTimes[1])
                        + "\ndelete: " + sw.chooseTimePrefix(avlTimes[2]) + "\nheight: " + avlStatus);

        System.out.println("\nDiff (AVL - BST):");
        System.out.println("insert: " + sw.chooseTimePrefix(avlTimes[0] - bstTimes[0]) + "\nsearch: "
                + sw.chooseTimePrefix(avlTimes[1] - bstTimes[1])
                + "\ndelete: " + sw.chooseTimePrefix(avlTimes[2] - bstTimes[2]) + "\nheight: "
                + (avlStatus - bstStatus));
    }
}
