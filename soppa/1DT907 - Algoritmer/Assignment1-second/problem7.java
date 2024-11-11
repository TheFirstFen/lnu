package Assignment1;

import java.util.ArrayList;
import java.util.List;

public class problem7 {
    public static void main(String[] args) {
        List<Integer> sizeTests = new ArrayList<>();
        sizeTests.add(100);
        sizeTests.add(500);
        sizeTests.add(1000);
        sizeTests.add(2500);
        sizeTests.add(5000);
        sizeTests.add(7500);
        sizeTests.add(10000);
        List<Double> bruteres = new ArrayList<>();
        List<Double> cacheres = new ArrayList<>();
        for (Integer size : sizeTests) {
            sum3 stand = new sum3(size);
            Runnable code = () -> stand.calc3sum();
            //System.out.println("Time for 3sum with the arraysize of " + size);
            bruteres.add(Timeit.timeCode(code, 1, false));
            sum3caching cach = new sum3caching(size);
            Runnable qcode = () -> cach.calc3sum();
            //System.out.println("Time for 3sum with cache with the arraysize of " + size);
            cacheres.add(Timeit.timeCode(qcode, 1, false));
        }
        System.out.println("Brute force results: \n" + bruteres);
        System.out.println("With cache results: \n" + cacheres);
    }
}
