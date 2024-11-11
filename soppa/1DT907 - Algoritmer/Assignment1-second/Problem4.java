package Assignment1;

import java.util.Random;
import java.util.List;
import java.util.ArrayList;
public class Problem4 {
    public static void main(String[] args) {
        List<Integer> sizeTests = new ArrayList<>();
        sizeTests.add(10000);
        sizeTests.add(50000);
        sizeTests.add(100000);
        List<Integer> amountTests = new ArrayList<>();
        amountTests.add(10000);
        amountTests.add(30000);
        amountTests.add(50000);
        amountTests.add(70000);
        amountTests.add(90000);       
        for (Integer size : sizeTests) {
            List<Double> ufList = new ArrayList<>(); 
            List<Double> qufList = new ArrayList<>(); 
            for (Integer amount : amountTests) {
                Random random = new Random();
                UF uf = new UF(size);
                Runnable code = () -> uf.union(random.nextInt(size), random.nextInt(size));
                System.out.println("Time for union find with the arraysize of " + size + " and " + amount + " of unions:");
                ufList.add(Timeit.timeCode(code, amount, true));
                QUF quf = new QUF(size);
                Runnable qcode = () -> quf.union(random.nextInt(size), random.nextInt(size));
                System.out.println("Time for quick union find with the arraysize of " + size + " and " + amount + " unions:");
                qufList.add(Timeit.timeCode(qcode, amount, true));
            }
            System.out.println("uf List of results for arraysize of " + size + "\n" + ufList);
            System.out.println("quf List of results for arraysize of " + size + "\n" + qufList);
        }
    }
}
