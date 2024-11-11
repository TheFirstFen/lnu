package Assignment2;

import java.util.Random;
import java.util.List;
import java.util.ArrayList;;


public class Problem3 {
    public static void main(String[] args) {
        List<Double> insertTimes = new ArrayList<>();
        System.out.print("Time for 1000 inserts ");
        insertTimes.add(Timeit.timeCode(() -> runInsertTest(1000), 1, true));
        System.out.print("Time for 5000 inserts ");
        insertTimes.add(Timeit.timeCode(() -> runInsertTest(5000), 1, true));
        System.out.print("Time for 10000 inserts ");
        insertTimes.add(Timeit.timeCode(() -> runInsertTest(10000), 1, true));
        System.out.print("Time for 50000 inserts ");
        insertTimes.add(Timeit.timeCode(() -> runInsertTest(50000), 1, true));
        System.out.print("Time for 100000 inserts ");
        insertTimes.add(Timeit.timeCode(() -> runInsertTest(100000), 1, true));
        System.out.print("Time for 250000 inserts ");
        insertTimes.add(Timeit.timeCode(() -> runInsertTest(250000), 1, true));
        System.out.print("Time for 500000 inserts ");
        insertTimes.add(Timeit.timeCode(() -> runInsertTest(500000), 1, true));
        System.out.println("----------------------------");
        List<Double> getPersonTimes = new ArrayList<>();
        final PQAsHeap PrioQueue = new PQAsHeap();
        Random random = new Random();
        for (int i = 0; i < 1000; i ++) {
            PrioQueue.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for 500 gets in a queue with 1000 persons ");
        getPersonTimes.add(Timeit.timeCode(() -> runGetTest(PrioQueue, 500), 1, true));
        
        final PQAsHeap pqbst2 = new PQAsHeap();
        for (int i = 0; i < 5000; i ++) {
            pqbst2.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for 2500 gets in a queue with 5000 persons ");
        getPersonTimes.add(Timeit.timeCode(() -> runGetTest(pqbst2, 2500), 1, true));
        
        final PQAsHeap pqbst3 = new PQAsHeap();
        for (int i = 0; i < 10000; i ++) {
            pqbst3.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for 5000 gets in a queue with 10000 persons ");
        getPersonTimes.add(Timeit.timeCode(() -> runGetTest(pqbst3, 5000), 1, true));

        final PQAsHeap pqbst4 = new PQAsHeap();
        for (int i = 0; i < 50000; i ++) {
            pqbst4.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for 25000 gets in a queue with 50000 persons ");
        getPersonTimes.add(Timeit.timeCode(() -> runGetTest(pqbst4, 25000), 1, true));

        final PQAsHeap pqbst5 = new PQAsHeap();
        for (int i = 0; i < 100000; i ++) {
            pqbst5.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for 50000 gets in a queue with 100000 persons ");
        getPersonTimes.add(Timeit.timeCode(() -> runGetTest(pqbst5, 50000), 1, true));
        final PQAsHeap pqbst50 = new PQAsHeap();
        for (int i = 0; i < 250000; i ++) {
            pqbst50.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for 125000 gets in a queue with 250000 persons ");
        getPersonTimes.add(Timeit.timeCode(() -> runGetTest(pqbst50, 125000), 1, true));

        final PQAsHeap pqbst6 = new PQAsHeap();
        for (int i = 0; i < 500000; i ++) {
            pqbst6.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for 250000 gets in a queue with 500000 persons ");
        getPersonTimes.add(Timeit.timeCode(() -> runGetTest(pqbst6, 250000), 1, true));
        System.out.println("----------------------------");
        List<Double> delMaxTimes = new ArrayList<>();
        final PQAsHeap pqbst21 = new PQAsHeap();
        random = new Random();
        for (int i = 0; i < 10000; i ++) {
            pqbst21.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for delmax with 1000 elements ");
        delMaxTimes.add(Timeit.timeCode(() -> runDelMaxTest(pqbst21), 1, true));
        
        final PQAsHeap pqbst22 = new PQAsHeap();
        for (int i = 0; i < 10000; i ++) {
            pqbst22.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for delmax with 5000 elements ");
        delMaxTimes.add(Timeit.timeCode(() -> runDelMaxTest(pqbst22), 1, true));
        
        final PQAsHeap pqbst23 = new PQAsHeap();
        for (int i = 0; i < 10000; i ++) {
            pqbst23.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for delmax with 10000 elements ");
        delMaxTimes.add(Timeit.timeCode(() -> runDelMaxTest(pqbst23), 1, true));

        final PQAsHeap pqbst24 = new PQAsHeap();
        for (int i = 0; i < 50000; i ++) {
            pqbst24.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for delmax with 50000 elements ");
        delMaxTimes.add(Timeit.timeCode(() -> runDelMaxTest(pqbst24), 1, true));

        final PQAsHeap pqbst25 = new PQAsHeap();
        for (int i = 0; i < 100000; i ++) {
            pqbst25.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for delmax with 100000 elements ");
        delMaxTimes.add(Timeit.timeCode(() -> runDelMaxTest(pqbst25), 1, true));
        
        final PQAsHeap pqbst250 = new PQAsHeap();
        for (int i = 0; i < 250000; i ++) {
            pqbst250.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for delmax with 250000 elements ");
        delMaxTimes.add(Timeit.timeCode(() -> runDelMaxTest(pqbst250), 1, true));

        final PQAsHeap pqbst26 = new PQAsHeap();
        for (int i = 0; i < 500000; i ++) {
            pqbst26.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for delmax with 500000 elements ");
        delMaxTimes.add(Timeit.timeCode(() -> runDelMaxTest(pqbst26), 1, true));
        System.out.println("----------------------------");
        List<Double> swapPrioTimes = new ArrayList<>();
        final PQAsHeap pqbstSwap = new PQAsHeap();
        for (int i = 0; i < 1000; i++) {
            pqbstSwap.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for swapprio with 1000 elements ");
        swapPrioTimes.add(Timeit.timeCode(() -> runSwapPrioTest(pqbstSwap, "Person0", "Person1"), 1, true));

        final PQAsHeap pqbstSwap2 = new PQAsHeap();
        for (int i = 0; i < 5000; i++) {
            pqbstSwap2.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for swapprio with 5000 elements ");
        swapPrioTimes.add(Timeit.timeCode(() -> runSwapPrioTest(pqbstSwap2, "Person0", "Person1"), 1, true));

        final PQAsHeap pqbstSwap3 = new PQAsHeap();
        for (int i = 0; i < 10000; i++) {
            pqbstSwap3.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for swapprio with 10000 elements ");
        swapPrioTimes.add(Timeit.timeCode(() -> runSwapPrioTest(pqbstSwap3, "Person0", "Person1"), 1, true));

        final PQAsHeap pqbstSwap4 = new PQAsHeap();
        for (int i = 0; i < 50000; i++) {
            pqbstSwap4.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for swapprio with 50000 elements ");
        swapPrioTimes.add(Timeit.timeCode(() -> runSwapPrioTest(pqbstSwap4, "Person0", "Person1"), 1, true));

        final PQAsHeap pqbstSwap5 = new PQAsHeap();
        for (int i = 0; i < 100000; i++) {
            pqbstSwap5.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for swapprio with 100000 elements ");
        swapPrioTimes.add(Timeit.timeCode(() -> runSwapPrioTest(pqbstSwap5, "Person0", "Person1"), 1, true));
        
        final PQAsHeap pqbstSwap50 = new PQAsHeap();
        for (int i = 0; i < 250000; i++) {
            pqbstSwap50.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for swapprio with 250000 elements ");
        swapPrioTimes.add(Timeit.timeCode(() -> runSwapPrioTest(pqbstSwap50, "Person0", "Person1"), 1, true));

        final PQAsHeap pqbstSwap6 = new PQAsHeap();
        for (int i = 0; i < 500000; i++) {
            pqbstSwap6.insert_person("Person" + i, random.nextInt(20));
        }
        System.out.print("Time for swapprio with 500000 elements ");
        swapPrioTimes.add(Timeit.timeCode(() -> runSwapPrioTest(pqbstSwap6, "Person0", "Person1"), 1, true));
        System.out.println("----------------------------");

        System.out.println("Insert:");
        System.out.println(insertTimes);
        System.out.println("Gets:");
        System.out.println(getPersonTimes);
        System.out.println("delMax:");
        System.out.println(delMaxTimes);
        System.out.println("Swap:");
        System.out.println(swapPrioTimes);
    }
    

    public static void runInsertTest(int numElements) {
     PQAsHeap PrioQueue = new PQAsHeap();
        Random random = new Random();
        for (int i = 0; i < numElements; i ++) {
            PrioQueue.insert_person("Person" + i, random.nextInt(5));
        }
    }
    public static void runGetTest (PQAsHeap PrioQueue, int getAmount) {
        for (int i = 0;i < getAmount; i ++) {
            PrioQueue.get_person();
        }
    }
    public static void runDelMaxTest (PQAsHeap PrioQueue) {
        PrioQueue.delete_max_prio();
    }
    public static void runSwapPrioTest (PQAsHeap PrioQueue, String name1, String name2) {
        PrioQueue.swap_priority(name1, name2);
    }
}