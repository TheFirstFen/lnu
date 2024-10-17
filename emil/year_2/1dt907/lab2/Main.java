import Algorithm.*;

import java.util.Random;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;
import java.util.Arrays;

public class Main {
    private static int randomQueueSize = 100; // Uppgift 1

    private static int tree_size = 1_000_000; // Uppgift 2
    private static int rand_val = 1_000_000; // Uppgift 2
    
    private static int amount_of_people = 1_000_000; // Uppgift 3
    private static int priority = 1_000; // Uppgift 3

    private static int arraysize = 500_000; // Uppgift 4
    private static int max_depth = 200; // Uppgift 4
    private static int heap_won = 0; // Uppgift 4
    private static int insert_won = 0; // Uppgift 4

    public static void main(String[] args) {
        //p1();

        //p2();
        
        //p2Test();    //Change the tree_size to 10_000 to run else stackoverflowError
        
        //p3();

        p4();
    
    }

    public static void p1() {
        System.out.println("\nUppgift 1");
        RandomQueue<Integer> randomQueue = new RandomQueue<>();
        System.out.println("Queue is empty: " + randomQueue.isEmpty());
        System.out.println("Queue size: " + randomQueue.size());
        for (int i = 0; i < randomQueueSize; i++) {
            randomQueue.enqueue(i);
        }
        System.out.println();
        RandomQueue.printQueue(randomQueue);
        System.out.println("Queue is empty: " + randomQueue.isEmpty());
        System.out.println("Queue size: " + randomQueue.size());
        for (int i = 0; i < randomQueueSize/2; i++) {
            randomQueue.dequeue();
        }
        System.out.println();
        RandomQueue.printQueue(randomQueue);
        System.out.println();
        System.err.println("Queue size: " + randomQueue.size());
    }

    public static void p2() {
        System.out.println("\nUppgift 2");
        List<Double> bstT = new ArrayList<>();
        List<Double> avlT = new ArrayList<>();

        Timer timer = new Timer();
        BSTree bst = new BSTree();
        AvlTree avl = new AvlTree();
        Random random = new Random();

        List<Integer> randomValues = new ArrayList<>();
        Double time = 0.0;

        int randVal;
        for (int i = 0; i < tree_size; i++) {
            randVal = random.nextInt(rand_val);
            randomValues.add(randVal);
        }

        // Insert
        for (int value : randomValues) {
            timer.Start();
            bst.insert(value);
            timer.Stop();
            time += timer.getnanoSecond() / 1_000_000;
            timer.RestartTimer();
        }
        bstT.add(time);
        time = 0.0;

        for (int value : randomValues) {
            timer.Start();
            avl.insert(value);
            timer.Stop();
            time += timer.getnanoSecond() / 1_000_000;

            timer.RestartTimer();
        }
        avlT.add(time);
        time = 0.0;

        // Search
        randVal = random.nextInt(rand_val);
        timer.Start();
        bst.search(randVal);
        timer.Stop();
        time += timer.getnanoSecond() / 1_000;
        timer.RestartTimer();
        bstT.add(time);
        time = 0.0;

        timer.Start();
        avl.search(randVal);
        timer.Stop();
        time += timer.getnanoSecond() / 1_000;
        timer.RestartTimer();
        avlT.add(time);
        time = 0.0;

        // Delete
        randVal = random.nextInt(rand_val);
        timer.Start();
        bst.search(randVal);
        timer.Stop();
        time += timer.getnanoSecond() / 1_000;
        timer.RestartTimer();
        bstT.add(time);
        
    
        timer.Start();
        avl.delete(randVal);
        timer.Stop();
        time += timer.getnanoSecond() / 1_000;
        timer.RestartTimer();
        avlT.add(time);

        System.out.println("Amount of tree nodes: " + tree_size);
        System.out.println("BST:");
        System.out.println("Total insertion time: " + bstT.get(0) + " milli seconds");
        System.out.println("Search time: " + bstT.get(1) + " micro seconds");
        System.out.println("Delete time: " + bstT.get(2) + " micro seconds");
        System.out.println("height: " + bst.height() + "\n");

        System.out.println("AVL:");
        System.out.println("Total insertion time: " + avlT.get(0) + " milli seconds");
        System.out.println("Search time: " + avlT.get(1) + " micro seconds");
        System.out.println("Delete time: " + avlT.get(2) + " micro seconds");
        System.out.println("height: " + avl.treeheight() + "\n");

        System.out.println("Diff BST - AVL: ");
        System.out.println("insertion: " + (bstT.get(0) - avlT.get(0)) + " milli seconds");
        System.out.println("search: " + (bstT.get(1) - avlT.get(1)) + " micro seconds");
        System.err.println("delete: " + (bstT.get(2) - avlT.get(2)) + " micro seconds");
        System.out.println("height: " + (bst.height() - avl.treeheight()));
    }

    public static void p3() {
        System.out.println("\nUppgift 3");
        Timer timer = new Timer();
        Ticket ticket = new Ticket();
        Random random = new Random();

        int j = 0;
        List<Double> person_time = new ArrayList<>();
        Double time = 0.0;

        for (int i = 0; i < amount_of_people; i++) {
            int b = random.nextInt(0, priority);
            ticket.insertPerson("Person" + i, b, i);
            j++;
        }
        int nextperson = amount_of_people+1;
        timer.Start();
        ticket.insertPerson("Person" + nextperson, 5, j);
        timer.Stop();
        time = timer.getnanoSecond()/1_000;
        person_time.add(time);
        timer.RestartTimer();
        time = 0.0;

        timer.Start();
        ticket.getPerson();
        timer.Stop();
        time += timer.getnanoSecond() / 1_000;
        timer.RestartTimer();
        person_time.add(time);
        time = 0.0;

        timer.Start();
        ticket.deleteMaxPriority();
        timer.Stop();
        time += timer.getnanoSecond() / 1_000;
        timer.RestartTimer();
        person_time.add(time);
        time = 0.0;

        timer.Start();
        ticket.swapPriority("Person1", "Person2");
        timer.Stop();
        time += timer.getnanoSecond() / 1_000;
        timer.RestartTimer();
        person_time.add(time);
        time = 0.0;

        System.out.println("\nQueue for tickets with " + amount_of_people + " people");
        System.out.println("Testing insert person: "+ person_time.get(0) + " micro seconds");
        System.out.println("Testing get person: "+ person_time.get(1) + " micro seconds");
        System.out.println("Testing delete max priority: "+ person_time.get(2) + " micro seconds");
        System.out.println("Testing swap priority: "+ person_time.get(3) + " micro seconds");
        ticket.printfirst10queue();

    }

    public static void p4() {
        System.out.println("\nUppgift 4");
        Timer timer = new Timer();
        Random random = new Random();
        Double insertTime = 0.0;
        Double heapTime = 0.0;
        int[] for_Quick = new int[arraysize];
        int[] for_heap = new int[arraysize];
        int[] for_insert = new int[arraysize];

        List<Double> HeapTimes = new ArrayList<>();
        List<Double> InsertTimes = new ArrayList<>();
        List<Integer> RecomendedDepths = new ArrayList<>();

        System.out.println("Arraysize: " + arraysize);
        for (int depth = 0; depth <= max_depth; depth+=5) {
            for (int i = 0; i < arraysize; i++) {
                int a = random.nextInt(arraysize);
                for_Quick[i] = a;
            }

            System.out.println("depth: " + depth);
            int[] quickSorted = QuickSort.quickSort(for_insert, depth);
            for_heap = Arrays.copyOf(quickSorted, quickSorted.length);
            for_insert = Arrays.copyOf(quickSorted, quickSorted.length);
            System.out.println("\nQuickSort done:");

            timer.Start();
            HeapSort.heapSort(for_Quick);
            timer.Stop();
            insertTime = timer.getnanoSecond() / 1_000;
            HeapTimes.add(heapTime);
            timer.RestartTimer();

            timer.Start();
            InsertionSort.insertionSort(for_heap);
            timer.Stop();
            heapTime = timer.getnanoSecond() / 1_000;
            InsertTimes.add(insertTime);
            timer.RestartTimer();

            System.out.println(insertTime);
            System.out.println(heapTime);

            faster(insertTime, heapTime);
            heapTime = 0.0;
            insertTime = 0.0;
            RecomendedDepths.add(depth);

        }
        double minHeapTime = Collections.min(HeapTimes);
        int minHeapDepth = RecomendedDepths.get(HeapTimes.indexOf(minHeapTime));

        // Find the minimum time for InsertionSort and corresponding depth
        double minInsertTime = Collections.min(InsertTimes);
        int minInsertDepth = RecomendedDepths.get(InsertTimes.indexOf(minInsertTime));

        System.out.println("heap won: " + heap_won);
        System.out.println("insert won: " + insert_won);

        System.out.println("Recomended depth for HeapSort: " + minHeapDepth);
        System.out.println("Recomended depth for InsertSort: " + minInsertDepth);
    }

    public static void faster(Double instetTime, Double heapTime) {
        if (heapTime < instetTime) {
            System.out.println("Heap is faster");
            heap_won += 1;
        } 
        else if (heapTime > instetTime) {
            System.out.println("Insert is faster");
            insert_won += 1;
        }
        else {
            System.out.println("They are equal");
        }
    }

    public static void p2Test() {
        System.out.println("\nUppgift 2 Test");
        List<Double> bstT = new ArrayList<>();
        List<Double> avlT = new ArrayList<>();

        Timer timer = new Timer();
        BSTree bst = new BSTree();
        AvlTree avl = new AvlTree();
        Random random = new Random();

        List<Integer> randomValues = new ArrayList<>();
        Double time = 0.0;

        int randVal;
        for (int i = 0; i < tree_size; i++) {
            randomValues.add(i);
        }

        // Insert
        for (int value : randomValues) {
            timer.Start();
            bst.insert(value);
            timer.Stop();
            time += timer.getnanoSecond() / 1_000_000;
            timer.RestartTimer();
        }
        bstT.add(time);
        time = 0.0;

        for (int value : randomValues) {
            timer.Start();
            avl.insert(value);
            timer.Stop();
            time += timer.getnanoSecond() / 1_000_000;

            timer.RestartTimer();
        }
        avlT.add(time);
        time = 0.0;

        // Search
        randVal = random.nextInt(rand_val);
        timer.Start();
        bst.search(randVal);
        timer.Stop();
        time += timer.getnanoSecond() / 1_000;
        timer.RestartTimer();
        bstT.add(time);
        time = 0.0;

        timer.Start();
        avl.search(randVal);
        timer.Stop();
        time += timer.getnanoSecond() / 1_000;
        timer.RestartTimer();
        avlT.add(time);
        time = 0.0;

        // Delete
        randVal = random.nextInt(rand_val);
        timer.Start();
        bst.search(randVal);
        timer.Stop();
        time += timer.getnanoSecond() / 1_000;
        timer.RestartTimer();
        bstT.add(time);
        
    
        timer.Start();
        avl.delete(randVal);
        timer.Stop();
        time += timer.getnanoSecond() / 1_000;
        timer.RestartTimer();
        avlT.add(time);

        System.out.println("Amount of tree nodes: " + tree_size);
        System.out.println("BST:");
        System.out.println("Total insertion time: " + bstT.get(0) + " milli seconds");
        System.out.println("Search time: " + bstT.get(1) + " micro seconds");
        System.out.println("Delete time: " + bstT.get(2) + " micro seconds");
        System.out.println("height: " + bst.height() + "\n");

        System.out.println("AVL:");
        System.out.println("Total insertion time: " + avlT.get(0) + " milli seconds");
        System.out.println("Search time: " + avlT.get(1) + " micro seconds");
        System.out.println("Delete time: " + avlT.get(2) + " micro seconds");
        System.out.println("height: " + avl.treeheight() + "\n");

        System.out.println("Diff BST - AVL: ");
        System.out.println("insertion: " + (bstT.get(0) - avlT.get(0)) + " milli seconds");
        System.out.println("search: " + (bstT.get(1) - avlT.get(1)) + " micro seconds");
        System.err.println("delete: " + (bstT.get(2) - avlT.get(2)) + " micro seconds");
        System.out.println("height: " + (bst.height() - avl.treeheight()));
    }
}
