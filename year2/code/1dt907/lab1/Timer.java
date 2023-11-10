import java.lang.System;

// * Problem 3
public class Timer {
    private long startTime;
    private long endTime;

    public void start() {
        startTime = System.nanoTime();
    }

    public void stop() {
        endTime = System.nanoTime();
    }

    public void reset() {
        startTime = 0;
        endTime = 0;
    }

    public double getTimeInNanoSeconds() {
        if (startTime == 0 || endTime == 0) {
            throw new IllegalStateException("Timer hasn't been used.");
        }
        return endTime - startTime;
    }

    public double getTimeInMicroSeconds() {
        return getTimeInNanoSeconds() / 1_000.0;
    }

    public double getTimeInMilliSeconds() {
        return getTimeInNanoSeconds() / 1_000_000.0;
    }

    public double getTimeInSeconds() {
        return getTimeInNanoSeconds() / 1_000_000_000.0;
    }
}
