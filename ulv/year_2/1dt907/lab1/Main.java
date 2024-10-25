import Algorithmer.*;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Timer timer = new Timer();
        List<Double> ufTimes = new ArrayList<>();
        List<Double> wqufTimes = new ArrayList<>();
        List<Double> sum3Times = new ArrayList<>();
        List<Double> sum3TwoPointerTimes = new ArrayList<>();

        for (int i = 100_000; i < 1_000_000; i += 100_000) {
            for(int size = 10_000; size < 100_000; size += 10_000) {
                UF uf = new UF(i);
                timer.Start();
                uf.randomUnion(uf, size);
                timer.Stop();
                System.out.println("Elements in array: " + i);
                System.out.println("The amount of unions : " + size);
                ufTimes.add(timer.getMilliSecond());

                System.out.println("UF");                
                Main.chooseTime(timer);
                timer.RestartTimer();

                WQUF wquf = new WQUF(i);
                timer.Start();
                wquf.randomWQUnion(wquf, size);
                timer.Stop();
                wqufTimes.add(timer.getMilliSecond());

                System.out.println("WQUF");
                Main.chooseTime(timer);
                timer.RestartTimer();
                System.out.println();
            }
        }
        for (int i = 0; i <10; i++) {
            for (int j = 500; j <= 5000; j += 500) {

                Sum3 sum3 = new Sum3();
                sum3.init(j);
                timer.Start();
                sum3.find3sum();
                timer.Stop();
                System.out.println("sum 3: ");
                Main.chooseTime(timer);
                sum3Times.add(timer.getMilliSecond());
                timer.RestartTimer();

                Sum3twoPointer sum3two = new Sum3twoPointer();
                sum3two.init(j);
                timer.Start();
                sum3two.find3sum2pointer();
                timer.Stop();
                System.out.println("sum 3 two pointer:");
                Main.chooseTime(timer);
                sum3TwoPointerTimes.add(timer.getMilliSecond());
                timer.RestartTimer();

                System.out.println();
            }
        }

        System.out.println("List of UF times: ");
        System.out.println(ufTimes);
        System.out.println();
        System.out.println("List of WQUF times: ");
        System.out.println(wqufTimes);
        System.out.println();
        System.out.println("List of Sum3 times: ");
        System.out.println(sum3Times);
        System.out.println();
        System.out.println("List of Sum3twoPointer times: ");
        System.out.println(sum3TwoPointerTimes);
        System.out.println();
    }

    public static void chooseTime(Timer timer) {
        if (timer.getMilliSecond() < 1_000){
            System.out.println("Time in milliseconds is: " + timer.getMilliSecond());
        }
        else {
            System.out.println("Time in seconds is: " + timer.getSecond());
        }
    }
}