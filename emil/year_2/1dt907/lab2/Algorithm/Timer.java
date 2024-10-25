package Algorithm;

import java.lang.System;

public class Timer {

    private static long startTime;
    private static long endTime;

    public void Start() {
        startTime = System.nanoTime();
    }

    public void Stop() {
        endTime = System.nanoTime();
    }

    public void RestartTimer() {
        startTime = 0;
        endTime = 0;
    }


    public double getSecond() {
        return (endTime - startTime)/1_000_000_000.0;
    }

     public double getMilliSecond() {
        return (endTime - startTime)/1_000_000.0;
    }

    public double getnanoSecond() {
        return (endTime - startTime)/1.0;
    }
}
