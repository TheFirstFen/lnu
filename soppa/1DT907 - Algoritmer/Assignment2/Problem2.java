package Assignment2;

import java.util.ArrayList;
import java.util.Random;
import java.util.List;

public class Problem2 {
    public static void main(String[] args) {
        int amount = 1024;
        List<Integer> rangeList = new ArrayList<>();
        for (int i = 1; i <= amount; i++) {
            rangeList.add(i);
        }

        Runnable codeBST = () -> {
            int bstsum = 0;
            for (int i = 0; i < 5000; i++) {
                BST bst = new BST();
                List<Integer> randomSample = getRandomSample(rangeList, 256);

                for (int v : randomSample) {
                    bst.insert(v);
                }

                List<Integer> deleteSample = getRandomSample(randomSample, 256);
                for (int v : deleteSample) {
                    bst.delete(v);
                }
                bstsum = bstsum + bst.getDepth();
            }
            System.out.println("Average height of BST trees (random input):");
            System.out.println(bstsum / 5000);
        };

        Runnable codeAVL = () -> {
            int avlsum = 0;
            for (int i = 0; i < 5000; i++) {
                AVLTree avl = new AVLTree();
                List<Integer> randomSample = getRandomSample(rangeList, 256);

                for (int v : randomSample) {
                    avl.add(v);
                }

                List<Integer> deleteSample = getRandomSample(randomSample, 256);
                for (int v : deleteSample) {
                    avl.delete(v);
                }
                avlsum = avlsum + avl.getTreeheight();
            }
            System.out.println("Average height of AVL trees (random input):");
            System.out.println(avlsum / 5000);
        };
        System.out.println("Time to create 5000 BST trees (random input): " + Timeit.timeCode(codeBST, 1, false));
        System.out.println("Time to create 5000 AVL trees (random input): " + Timeit.timeCode(codeAVL, 1, false));

        Runnable codeBSTSorted = () -> {
            int bstSum = 0;
            for (int i = 0; i < 5000; i++) {
                BST bst = new BST();
                for (int v : rangeList) {
                    bst.insert(v);
                }
                bstSum += bst.getDepth();
            }
            System.out.println("Average height of BST trees (sorted input):");
            System.out.println(bstSum / 5000);
        };

        Runnable codeAVLSorted = () -> {
            int avlSum = 0;
            for (int i = 0; i < 5000; i++) {
                AVLTree avl = new AVLTree();
                for (int v : rangeList) {
                    avl.add(v);
                }
                avlSum += avl.getTreeheight();
            }
            System.out.println("Average height of AVL trees (sorted input):");
            System.out.println(avlSum / 5000);
        };

        System.out.println("Time to create 5000 BST trees (sorted input): " + Timeit.timeCode(codeBSTSorted, 1, false));

        System.out.println("Time to create 5000 AVL trees (sorted input): " + Timeit.timeCode(codeAVLSorted, 1, false));
    }
    

    private static List<Integer> getRandomSample(List<Integer> l, int k) {
        List<Integer> sample = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < k; i++) {
            int randomIndex = random.nextInt(l.size());
            sample.add(l.get(randomIndex));
        }
        return sample;
    }
}

